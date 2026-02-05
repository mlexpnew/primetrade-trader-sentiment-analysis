import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Trader Performance vs Market Sentiment")

data = pd.read_csv("final_df.csv")

sentiment = st.selectbox("Select Sentiment", data['classification'].unique())

filtered = data[data['classification'] == sentiment]

st.metric("Average Daily PnL", round(filtered['daily_pnl'].mean(), 2))
st.metric("Average Trades per Day", round(filtered['trades_count'].mean(), 2))

fig, ax = plt.subplots()
sns.boxplot(data=filtered, x='classification', y='daily_pnl', ax=ax)
st.pyplot(fig)
