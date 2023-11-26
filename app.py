import streamlit as st
import pandas as pd
import plotly.express as px
games = pd.read_csv(r'C:\Users\James\Project_games\games.csv')

st.header('Video Game Sales Analysis')

st.subheader('Distribution of Total Sales')
total_sales_hist = px.histogram(df, x='total_sales')
st.plotly_chart(total_sales_hist)

st.subheader('User Score vs Total Sales')
user_score_scatter = px.scatter(df, x='user_score', y='total_sales', trendline="ols")
st.plotly_chart(user_score_scatter)

if st.checkbox('Show Scatter Plot of Critic Score vs Total Sales'):
    st.subheader('Critic Score vs Total Sales')
    critic_score_scatter = px.scatter(df, x='critic_score', y='total_sales', trendline="ols")
    st.plotly_chart(critic_score_scatter)