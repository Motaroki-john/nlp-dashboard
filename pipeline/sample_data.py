import os
import sqlite3


os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/social_media_data.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY,
    text TEXT,
    user TEXT,
    timestamp TEXT
)
""")


sample_posts = [
    ("1", "I love the new AI technology advancements that are revolutionizing industries with innovative solutions every day, transforming how we work and live!", "user1", "2025-06-12 10:00:00"),
    ("2", "This tech conference was a total disaster with poor organization, unengaging speakers, and technical issues that ruined the entire experience for attendees.", "user2", "2025-06-12 10:05:00"),
    ("3", "AI is changing the world, but it’s neutral so far with both positive impacts like automation and negative ones like job displacement across various sectors globally.", "user3", "2025-06-12 10:10:00"),
    ("4", "Excited about the latest innovations in tech that promise to transform healthcare and education with cutting-edge tools and improved accessibility for all!", "user4", "2025-06-12 10:15:00"),
    ("5", "Tech support failed me again, so frustrated with the slow response and lack of effective solutions provided today despite multiple attempts to resolve the issue.", "user5", "2025-06-12 10:20:00")
]


cursor.executemany("INSERT OR IGNORE INTO posts (id, text, user, timestamp) VALUES (?, ?, ?, ?)", sample_posts)
conn.commit()
conn.close()
print(" Sample data inserted into data/social_media_data.db")
