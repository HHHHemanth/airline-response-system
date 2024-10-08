# ml_model.py
import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    """Analyze sentiment of the text and return 'Positive', 'Negative', or 'Neutral'."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_feedback(file_path):
    """Read feedback data from a CSV file and analyze sentiment."""
    # Load dataset
    df = pd.read_csv(file_path)

    # Check if 'feedback' column exists
    if 'feedback' not in df.columns:
        raise ValueError("CSV file must contain a 'feedback' column")

    # Apply sentiment analysis
    df['Sentiment'] = df['feedback'].apply(get_sentiment)

    # Return DataFrame with results
    return df[['feedback', 'Sentiment']]
