from transformers import pipeline
import sqlite3

# Initialize sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Connect to database
conn = sqlite3.connect("data/social_media_data.db")
cursor = conn.cursor()

# Add sentiment column if not exists
try:
    cursor.execute("ALTER TABLE posts ADD COLUMN sentiment TEXT")
    conn.commit()
except sqlite3.OperationalError:
    pass  # Column already exists

# Analyze sentiment
cursor.execute("SELECT id, text FROM posts WHERE sentiment IS NULL")
posts = cursor.fetchall()
for post_id, text in posts:
    result = sentiment_analyzer(text[:512])[0]  # Truncate to 512 tokens
    sentiment = result["label"]
    cursor.execute("UPDATE posts SET sentiment = ? WHERE id = ?", (sentiment, post_id))
    conn.commit()
conn.close()
print("Sentiment analysis completed.")