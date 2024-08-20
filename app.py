import os
from flask import Flask, request
from flask_restx import Api, Resource, fields
import pandas as pd
import numpy as np
from io import StringIO
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-Key'
    }
}
api = Api(app, version='1.0', title='Data Processing API',
          description='A simple API for data ingestion and processing',
          authorizations=authorizations,
          security='apikey')

data_storage = None
API_KEY = "othor"

ns_upload = api.namespace('upload', description='Data upload operations')
ns_stats = api.namespace('stats', description='Data statistics operations')
ns_query = api.namespace('query', description='Data query operations')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)

query_parser = api.parser()
query_parser.add_argument('column', type=str, required=True, help='Column name to filter')
query_parser.add_argument('value', type=str, required=True, help='Value to filter by')

def require_api_key(func):
    def check_api_key(*args, **kwargs):
        if request.headers.get('X-API-Key') and request.headers.get('X-API-Key') == API_KEY:
            return func(*args, **kwargs)
        api.abort(401, "API Key required")
    return check_api_key

@ns_upload.route('/')
class UploadCSV(Resource):
    @api.doc(parser=upload_parser)
    @api.doc(security='apikey')
    @require_api_key
    def post(self):
        """Upload a CSV file"""
        global data_storage
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        
        if uploaded_file.filename == '':
            api.abort(400, "No selected file")
        
        if not uploaded_file.filename.endswith('.csv'):
            api.abort(400, "File must be a CSV")
        
        try:
            content = uploaded_file.read().decode('utf-8')
            data_storage = pd.read_csv(StringIO(content))
            return {"message": "File uploaded successfully"}, 200
        except Exception as e:
            api.abort(400, f"Error processing file: {str(e)}")

@ns_stats.route('/')
class GetStats(Resource):
    @api.doc(security='apikey')
    @require_api_key
    def get(self):
        """Get statistics for numerical columns"""
        if data_storage is None:
            api.abort(404, "No data available")
        
        numeric_columns = data_storage.select_dtypes(include=[np.number]).columns
        stats = data_storage[numeric_columns].agg(['mean', 'median']).to_dict()
        return stats

@ns_query.route('/')
class QueryData(Resource):
    @api.doc(parser=query_parser)
    @api.doc(security='apikey')
    @require_api_key
    def get(self):
        """Query data by column and value"""
        if data_storage is None:
            api.abort(404, "No data available")
        
        args = query_parser.parse_args()
        column = args['column']
        value = args['value']

        numeric_cols=data_storage.select_dtypes(include=[np.number]).columns
        
        if column in numeric_cols:
            value=int(value)
        
        if column not in data_storage.columns:
            api.abort(400, f"Column '{column}' not found")
        
        filtered_data = data_storage[data_storage[column] == value]
        return filtered_data.to_dict(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
