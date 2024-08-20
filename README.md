API Documentation
Overview
This API provides tools to upload CSV files, generate summary statistics, and query specific rows. It is built using Flask and Pandas.

Requirements
Ensure you have Python installed on your machine, then install the necessary packages:

bash
Copy code
pip install flask pandas
How to Use
Run the Flask App:

Start the API by running the following command:

bash
Copy code
python app.py
The API will now be available at the specified address (e.g., http://localhost:5000).

Authorization:

To authorize, follow these steps:

Look for the "Authorize" button at the top right of the API documentation page (represented by a lock icon).
Click on the "Authorize" button to open a pop-up window.
In the pop-up window, enter your API key (othor) in the field labeled "Value" under "apikey (apiKey)".
Click the "Authorize" button in the pop-up and close the window. You are now authorized to use the API.
Using the Endpoints:

The API provides three main endpoints:

/upload: Upload a CSV file for summary and querying.
/stats: Get statistics of all numerical columns in the uploaded CSV.
/query: Specify a column name and value to retrieve the corresponding row.
To interact with each endpoint:

Click on the endpoint you wish to use.
Click the "Try it out" button.
Fill in the necessary details.
Click the "Execute" button to run the request
