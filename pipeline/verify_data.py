import sqlite3

# Connect to the database
conn = sqlite3.connect("data/social_media_data.db")
cursor = conn.cursor()

# Fetch and print posts
cursor.execute("SELECT * FROM posts LIMIT 5")
rows = cursor.fetchall()

print("Sample Posts from the Database:\n")
for row in rows:
    print(row)

conn.close()
