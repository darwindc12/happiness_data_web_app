import streamlit as st
import plotly.express as px
import pandas as pd

# Load dataframe
df = pd.read_csv("happy.csv")

# Add title widget
st.title("In Search for Happiness")
# Add two select box widget
x_axis = st.selectbox("Select the data for X-axis", sorted({"GDP", "Happiness", "Generosity"}))
y_axis = st.selectbox("Select the data for Y-axis", sorted({"GDP", "Happiness", "Generosity"}))


# Function pull the math data of x and y-axis selection
def get_data(x_local, y_local):
    # Match the value of first selection
    match x_local:
        case "GDP":
            x_list = df['gdp']
        case "Happiness":
            x_list = df["happiness"]
        case "Generosity":
            x_list = df["generosity"]
    # Match the value of second selection
    match y_local:
        case "GDP":
            y_list = df['gdp']
        case "Happiness":
            y_list = df["happiness"]
        case "Generosity":
            y_list = df["generosity"]

    return x_list, y_list


# Add subheader widget
st.subheader(f"{x_axis} and {y_axis}")

# Return values of get_data function
x, y = get_data(x_axis, y_axis)

# Create and add the plot to the web page
figure = px.scatter(x=x, y=y, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)