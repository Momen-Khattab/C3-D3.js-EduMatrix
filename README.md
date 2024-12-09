This project is a web application built using Flask, a popular Python web framework, combined with D3.js and C3.js, powerful JavaScript libraries for creating interactive data visualizations. The main goal of the project is to display insightful and dynamic visual representations of data stored in CSV files.

Key Features:
Dynamic Data Visualization:

The application uses D3.js to create customized, interactive charts such as bar charts and radial charts.
C3.js is integrated for easier chart generation with pre-built functionality, making it simple to bind data and render various types of charts, like bar, pie, and donut charts.
Data Loading:

The project loads data from CSV files, allowing for real-time analysis and visualization of the data without hard-coding values.
Responsive Design:

The application is designed to be responsive, ensuring that visualizations are accessible and functional across a variety of devices and screen sizes.
User Interaction:

Users can interact with the charts, such as hovering over elements to reveal tooltips and clicking on chart elements for additional information or actions.
Interactive features make it easier to explore trends and relationships within the data.
Flask Backend:

The Flask server handles data processing and serves the front-end web pages, connecting the D3.js and C3.js components seamlessly to render visual content.
The backend ensures that the application is scalable and can be extended with additional data processing capabilities as needed.
Files & Structure:
app.py: The main Python file running the Flask application, responsible for setting up routes and handling requests.
templates/:
index.html: The landing page of the app with links to different visualizations.
c3_graph.html: A page dedicated to a visualization built with C3.js.
d3_graph.html: A page featuring an advanced visualization using D3.js for more customizable visual representations.
static/:
css/styles.css: Custom styling for the app's frontend.
images/: Various images used within the app, including logos and background images.
worldometer_data.csv: A CSV data file used for testing and demonstrating visualizations.
Technologies Used:
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Visualization Libraries: D3.js, C3.js
Data Handling: CSV files
