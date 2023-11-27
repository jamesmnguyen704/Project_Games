import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
games = pd.read_csv('games.csv')

# Streamlit header
st.header('Video Game Sales Analysis')

# Histogram for distribution of total sales
st.subheader('Distribution of Total Sales')
total_sales_hist = px.histogram(games, x='total_sales')  # use 'games' instead of 'df'
st.plotly_chart(total_sales_hist)

# Scatter plot for User Score vs Total Sales
st.subheader('User Score vs Total Sales')
user_score_scatter = px.scatter(games, x='user_score', y='total_sales', trendline="ols")  # use 'games' instead of 'df'
st.plotly_chart(user_score_scatter)

# Checkbox to show/hide the scatter plot of Critic Score vs Total Sales
if st.checkbox('Show Scatter Plot of Critic Score vs Total Sales'):
    st.subheader('Critic Score vs Total Sales')
    critic_score_scatter = px.scatter(games, x='critic_score', y='total_sales', trendline="ols")  # use 'games' instead of 'df'
    st.plotly_chart(critic_score_scatter)
