import streamlit as st
import plotly.express as px


st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for X-axis", sorted({"GDP", "Happiness", "Generosity"}))
y_axis = st.selectbox("Select the data for Y-axis", sorted({"GDP", "Happiness", "Generosity"}))
st.subheader(f"{x_axis} and {y_axis}")

