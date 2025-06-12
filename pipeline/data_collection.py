import tweepy
import sqlite3
from datetime import datetime

# X API credentials 
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"
BEARER_TOKEN = "your_bearer_token"

# SQLite setup
conn = sqlite3.connect("data/social_media_data.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS posts
                 (id TEXT PRIMARY KEY, text TEXT, user TEXT, timestamp TEXT)""")
conn.commit()

# Streaming client
class PostStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        try:
            cursor.execute("INSERT OR IGNORE INTO posts (id, text, user, timestamp) VALUES (?, ?, ?, ?)",
                           (str(tweet.id), tweet.text, str(tweet.author_id), str(datetime.now())))
            conn.commit()
            print(f"Collected: {tweet.text[:50]}...")
        except Exception as e:
            print(f"Error: {e}")

# Initialize and run stream
stream = PostStream(bearer_token=BEARER_TOKEN)
stream.add_rule(tweepy.StreamRule("technology OR AI"))
stream.filter()