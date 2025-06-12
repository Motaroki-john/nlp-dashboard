from transformers import pipeline
import sqlite3

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Connect to database
conn = sqlite3.connect("data/social_media_data.db")
cursor = conn.cursor()

# Add summary column if not exists
try:
    cursor.execute("ALTER TABLE posts ADD COLUMN summary TEXT")
    conn.commit()
except sqlite3.OperationalError:
    pass  # Column already exists

# Summarize long posts
cursor.execute("SELECT id, text FROM posts WHERE length(text) > 280 AND summary IS NULL")
posts = cursor.fetchall()
for post_id, text in posts:
    summary = summarizer(text[:1024], max_length=60, min_length=20, do_sample=False)[0]["summary_text"]
    cursor.execute("UPDATE posts SET summary = ? WHERE id = ?", (summary, post_id))
    conn.commit()
conn.close()
print("Summarization completed.")