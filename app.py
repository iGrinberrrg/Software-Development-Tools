import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

# Adding a Title
st.header('Data Analysis with Plotly e Streamlit')

# Add a filter to select the condition of the car
condition_filter = st.selectbox(
    'Select Car Condition',
    ['All', 'new', 'like new', 'excellent', 'good', 'fair', 'salvage']
)

# Filter the data based on the selected condition
if condition_filter != 'All':
    df = df[df['condition'] == condition_filter]

# Scatterplots - fig1
# Year Model by Cylinders
fig1 = px.scatter(df, x='model_year', y='cylinders', title='Year Model by Cylinders',
                  labels={'model_year': 'Year Model', 'cylinders': 'Cylinders'})
st.plotly_chart(fig1)

# Histogram - fig2
# "model_year" distribution
fig2 = px.histogram(df, x='model_year', title='Distribution of Model Year', nbins=30)
fig2.update_xaxes(title='Model Year')
fig2.update_yaxes(title='Frequency')
st.plotly_chart(fig2)

# Histogram - fig3
# Distribution of Number of Cylinders
fig3 = px.histogram(df, x='cylinders', title='Distribution of Number of Cylinders', nbins=15)
fig3.update_xaxes(title='Number of Cylinders')
fig3.update_yaxes(title='Frequency')
st.plotly_chart(fig3)
