
import streamlit as st
import pandas as pd
import altair as alt

st.title('Sales Dashboard — Demo')

monthly = pd.read_csv('C:/Users/TOMBSTONE25/my_project/data/processed/monthly_revenue.csv', parse_dates=['month'])
st.header('Monthly Revenue')
chart = alt.Chart(monthly).mark_line(point=True).encode(x='month:T', y='revenue:Q', tooltip=['month','revenue'])
st.altair_chart(chart, use_container_width=True)

st.header('Top Customers')
top = pd.read_csv('C:/Users/TOMBSTONE25/my_project/data/processed/cohort_counts.csv', parse_dates=['cohort_month'])
st.write(top.head())
