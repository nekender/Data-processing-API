# API Documentation

This API provides functionalities to upload CSV files, generate statistical summaries, and query data. Follow the steps below to set up and use the API.

## Installation

1. Install the required packages:
    ```bash
    pip install flask pandas
    ```

2. Run the Flask app:
    ```bash
    python app.py
    ```

## Usage

After running the Flask app, the API will be available at http://127.0.0.1:5000/. Follow the steps below to authorize and use the endpoints.

### Authorization

1. Look for the "Authorize" button at the top right of the API documentation page. It should appear as a lock icon.
2. Click on the "Authorize" button to open a pop-up window.
3. In the pop-up, locate the field labeled "Value" under "apikey (apiKey)".
4. Enter your API key (`othor`) in this field.
5. Click the "Authorize" button in the pop-up and then close it. You are now authorized to use the API.

### Endpoints

The API provides three main endpoints:

1. **Upload CSV File**
    - **Endpoint:** `/upload`
    - **Description:** Upload a CSV file for summary and querying.

2. **Get Statistics**
    - **Endpoint:** `/stats`
    - **Description:** Retrieve statistics for all numerical columns in the uploaded CSV file.

3. **Query Data**
    - **Endpoint:** `/query`
    - **Description:** Specify a column name and value to retrieve the corresponding row from the uploaded CSV file.

### Running Endpoints

To run each endpoint:

1. Click on the endpoint in the API documentation.
2. Click on the "Try it out" button.
3. Fill in the required parameters (if any) and click "Execute" to run the endpoint.

## Conclusion

You should now be able to use the API for uploading CSV files, getting statistics, and querying data. Make sure to authorize yourself using the API key before accessing the endpoints.
