# In Search for Happiness
This code is a Streamlit app that loads a CSV file with data about happiness in different countries and displays a scatter plot of two selected variables.

## Requirements
To run this app you need to have the following packages installed:

* streamlit
* plotly
* pandas

You can install them using pip with the following command:

pip install streamlit plotly pandas

## Usage
To run the app, simply execute the app.py file and a web page will open displaying the scatter plot.

Two select boxes are available on the web page, where you can choose the data to be displayed on each axis. The available options are "GDP", "Happiness", and "Generosity".

The scatter plot will update automatically when a new selection is made.

## Code
The code uses Streamlit to create the web interface and Plotly to create the scatter plot. The CSV file is loaded using Pandas.

A function called get_data is defined to retrieve the data for the selected variables from the CSV file based on the user's selection.

The selected data is then used to create the scatter plot using Plotly's scatter function, which is then displayed on the web page using Streamlit's plotly_chart function.

## Future improvements
Add more data to the CSV file to increase the range of options for the select boxes.
Add more customization options to the scatter plot, such as changing the color and size of the markers based on a third variable.
