import gensim
from gensim import corpora
from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation
import nltk
from nltk.tokenize import word_tokenize
import sqlite3

# Preprocess text
def preprocess(text):
    text = strip_punctuation(text.lower())
    text = remove_stopwords(text)
    tokens = word_tokenize(text)
    return [token for token in tokens if len(token) > 2]

# Load data
conn = sqlite3.connect("data/social_media_data.db")
cursor = conn.cursor()
cursor.execute("SELECT text FROM posts")
texts = [row[0] for row in cursor.fetchall()]
conn.close()

# Create dictionary and corpus
processed_texts = [preprocess(text) for text in texts]
dictionary = corpora.Dictionary(processed_texts)
corpus = [dictionary.doc2bow(text) for text in processed_texts]

# Train LDA model
lda_model = gensim.models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

# Print and save topics
topics = []
for idx, topic in lda_model.print_topics(-1):
    topics.append(f"Topic {idx}: {topic}")
with open("data/topics.txt", "w") as f:
    f.write("\n".join(topics))
print("Topic modeling completed. Topics saved to data/topics.txt")