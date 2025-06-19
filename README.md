# NLP Dashboard

A Streamlit-based dashboard for analyzing social media data with sentiment analysis, topic modeling, and summarization.

## Overview
This project processes social media posts stored in a SQLite database (`social_media_data.db`) using pre-trained transformer models from Hugging Face. It provides a web interface to visualize sentiment distribution, recent posts, and extracted topics.

## Features
- Sentiment Analysis: Classifies posts as POSITIVE, NEGATIVE, or NEUTRAL using `distilbert-base-uncased-finetuned-sst-2-english`.
- Topic Modeling: Extracts topics from posts using `topic_modeling.py`.
- Summarization: Summarizes long posts (>280 characters) using `facebook/bart-large-cnn`.
- Dashboard: Displays results via Streamlit at `http://localhost:8502`.

## Prerequisites
- Python 3.11+ (download from https://www.python.org/downloads/ if needed, verify with `python --version`)
- Required packages: `transformers`, `torch`, `streamlit`, `sqlite3`, `pandas`, `scikit-learn`, `numpy`
- Install dependencies via: `pip install -r requirements.txt` (if the file is missing, use `pip install transformers torch streamlit sqlite3 pandas scikit-learn numpy`; upgrade pip with `pip install --upgrade pip` if errors occur)
- Hardware: 16GB RAM recommended, GPU optional for faster transformer inference
- Git (install from https://git-scm.com/downloads/ if needed, check with `git --version`)

## Setup
- Clone the repository: Navigate to your desired directory in a terminal (Command Prompt on Windows, Terminal on macOS/Linux, or Git Bash) with `cd /path/to/where/you/want/to/store/the/project`, then run `git clone https://github.com/Motoroki-john/nlp-dashboard.git` and move into the directory with `cd nlp-dashboard`.
- Set up a virtual environment: Run `python -m venv venv` and activate it with `source venv/bin/activate` on macOS/Linux or `venv\Scripts\activate` on Windows (look for the `(venv)` prompt).
- Obtain `social_media_data.db`: Ensure it’s included in the repository or download it from a provided link if external, placing it in the project root (include a schema or creation steps if applicable, e.g., `sqlite3 social_media_data.db < schema.sql`).
- Run the dashboard: Execute `streamlit run app.py` (adjust to the correct main file if different) to access it at `http://localhost:8502`; if port 8502 is in use, try `streamlit run app.py --server.port 8503`.

## Troubleshooting
- Missing database: Confirm `social_media_data.db` is in the project directory or follow setup steps to create it.
- Port conflict: Switch to a different port with `streamlit run app.py --server.port 8503`.
- Dependency issues: Reinstall with `pip install -r requirements.txt` after updating pip, or manually install missing packages.
- Slow performance: Use a GPU if available or consider a lighter model like `distilbert`.
