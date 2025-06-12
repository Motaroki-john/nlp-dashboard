import streamlit as st
import sqlite3
import pandas as pd

st.title("NLP Dashboard for Social Media")

# Load data
conn = sqlite3.connect("data/social_media_data.db")
df = pd.read_sql_query("SELECT text, sentiment, summary FROM posts", conn)
conn.close()

# Sentiment chart
st.subheader("Sentiment Distribution")
sentiment_counts = df["sentiment"].value_counts()
st.bar_chart(sentiment_counts)

# Recent posts
st.subheader("Recent Posts")
st.dataframe(df[["text", "sentiment", "summary"]].head(50))

# Display topics
st.subheader("Topics")
with open("data/topics.txt", "r") as f:
    topics = f.read()
st.text(topics)