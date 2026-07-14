import streamlit as st
import pandas as pd
import sqlite3

st.title("📈 Бизнес-аналитика: Поведение пользователей")

conn = sqlite3.connect("business_metrics.db")
df = pd.read_sql_query("SELECT * FROM user_behavior", conn)
conn.close()

st.subheader("Топ пользователей по риску оттока")
df['churn_risk'] = (1 - df['conversion_rate']) * df['revenue']
st.table(df.sort_values(by='churn_risk', ascending=False).head(5))

st.subheader("Выручка по пользователям")
st.bar_chart(df['revenue'])