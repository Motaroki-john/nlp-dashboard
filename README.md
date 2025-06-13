# NLP Dashboard

A Streamlit-based dashboard for analyzing social media data with sentiment analysis, topic modeling, and summarization.

## Overview
This project processes social media posts stored in a SQLite database (`social_media_data.db`) using pre-trained transformer models from Hugging Face. It provides a web interface to visualize sentiment distribution, recent posts, and extracted topics.

## Features
- **Sentiment Analysis**: Classifies posts as POSITIVE, NEGATIVE, or NEUTRAL using `distilbert-base-uncased-finetuned-sst-2-english`.
- **Topic Modeling**: Extracts topics from posts using `topic_modeling.py`.
- **Summarization**: Summarizes long posts (>280 characters) using `facebook/bart-large-cnn`.
- **Dashboard**: Displays results via Streamlit at `http://localhost:8502`.

## Prerequisites
- Python 3.11+
- Required packages: `transformers`, `torch`, `streamlit`, `sqlite3`, `pandas`, `scikit-learn`, `numpy`
- Install dependencies via:
  pip install -r requirements.txt