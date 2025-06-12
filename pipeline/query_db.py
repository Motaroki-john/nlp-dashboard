import sqlite3
from tabulate import tabulate  # For nice table formatting

# Connect to your database
conn = sqlite3.connect('C:/Users/HP/nlp_dashboard/data/social_media_data.db')
cursor = conn.cursor()

# Execute your query
cursor.execute("SELECT text, sentiment, summary FROM posts LIMIT 5")
results = cursor.fetchall()

# Print formatted results
print(tabulate(results, headers=["Text", "Sentiment"], tablefmt="grid"))

# Close connection
conn.close()