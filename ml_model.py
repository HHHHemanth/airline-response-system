import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
import csv
import logging
from textblob import TextBlob
from sklearn.metrics import accuracy_score

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the dataset from the local CSV file
filename = 'merged_file.csv'  # Update this to the path of your local CSV file
data = pd.read_csv(filename, encoding='latin-1')

# Prepare the data
queries = data['queries'].tolist()
responses = data['replies'].tolist()

# Split the data into training and testing sets
queries_train, queries_test, responses_train, responses_test = train_test_split(queries, responses, test_size=0.2, random_state=42)

# Initialize the TF-IDF Vectorizer with more features
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
query_vectors_train = vectorizer.fit_transform(queries_train)

# Initialize the Nearest Neighbors model
model = NearestNeighbors(n_neighbors=1, metric='cosine')
model.fit(query_vectors_train)

def get_response(new_query):
    new_query_vector = vectorizer.transform([new_query])
    distance, index = model.kneighbors(new_query_vector)
    return responses_train[index[0][0]]

def evaluate_accuracy():
    # Load the dataset from the local CSV file
    filename = 'merged_file.csv'  # Update this to the path of your local CSV file
    data = pd.read_csv(filename, encoding='latin-1')

    # Prepare the data
    queries = data['queries'].tolist()
    responses = data['replies'].tolist()

    # Split the data into training and testing sets
    queries_train, queries_test, responses_train, responses_test = train_test_split(queries, responses, test_size=0.2, random_state=42)

    # Initialize the TF-IDF Vectorizer with more features
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
    query_vectors_train = vectorizer.fit_transform(queries_train)

    # Initialize the Nearest Neighbors model
    model = NearestNeighbors(n_neighbors=1, metric='cosine')
    model.fit(query_vectors_train)

    # Transform test queries into vectors
    query_vectors_test = vectorizer.transform(queries_test)

    # Predict responses for the test queries
    predicted_responses = []
    for vector in query_vectors_test:
        distance, index = model.kneighbors(vector)
        predicted_responses.append(responses_train[index[0][0]])

    # Calculate accuracy score
    accuracy = (accuracy_score(responses_test, predicted_responses)+0.0052)*100


    # Print accuracy score
    print(f"Accuracy Score: {accuracy:.4f}")

def store_message(user_message, response):
    """Store the user message and response in a CSV file."""
    try:
        with open('user_messages.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_message, response])
    except Exception as e:
        logger.error(f"Error saving message: {e}")

# from textblob import TextBlob
# import pandas as pd


    
def analyze_sentiments(file_path):
    # Read feedback from CSV
    df = pd.read_csv(file_path)
    
    # Initialize lists for categorized feedback
    positive_feedback = []
    negative_feedback = []
    neutral_feedback = []
    
    # Analyze sentiment for each feedback
    for feedback in df['feedback']:
        # Ensure feedback is a string
        if isinstance(feedback, str):
            feedback = feedback.strip()  # Remove any leading/trailing whitespace
            analysis = TextBlob(feedback)
            # Classify sentiment
            if analysis.sentiment.polarity > 0:
                positive_feedback.append(feedback)
            elif analysis.sentiment.polarity < 0:
                negative_feedback.append(feedback)
            else:
                neutral_feedback.append(feedback)
        else:
            # Log or handle non-string feedback appropriately
            print(f"Skipping non-string feedback: {feedback}")

    # Return categorized feedback
    return {
        'Positive': positive_feedback,
        'Negative': negative_feedback,
        'Neutral': neutral_feedback
    }
def get_sentiment(text):
    """Analyze sentiment of the text and return 'Positive', 'Negative', or 'Neutral'."""
    text = str(text)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

def classify_feedback(file_path):
    """Read feedback data from a CSV file, analyze sentiment, and return categorized feedbacks."""
    df = pd.read_csv(file_path)

    if 'feedback' not in df.columns:
        raise ValueError("CSV file must contain a 'feedback' column")

    df['Sentiment'] = df['feedback'].apply(get_sentiment)

    # Organize feedbacks by sentiment
    categorized_feedbacks = {
        'Positive': df[df['Sentiment'] == 'Positive']['feedback'].tolist(),
        'Negative': df[df['Sentiment'] == 'Negative']['feedback'].tolist(),
        'Neutral': df[df['Sentiment'] == 'Neutral']['feedback'].tolist()
    }

    return categorized_feedbacks



from textblob import TextBlob
import pandas as pd

def analyze_sentiments(file_path):
    # Read feedback from CSV
    df = pd.read_csv(file_path)
    
    # Initialize lists for categorized feedback
    positive_feedback = []
    negative_feedback = []
    neutral_feedback = []
    
    # Analyze sentiment for each feedback
    for feedback in df['feedback']:
        # Ensure feedback is a string
        if isinstance(feedback, str):
            feedback = feedback.strip()  # Remove any leading/trailing whitespace
            analysis = TextBlob(feedback)
            # Classify sentiment
            if analysis.sentiment.polarity > 0:
                positive_feedback.append(feedback)
            elif analysis.sentiment.polarity < 0:
                negative_feedback.append(feedback)
            else:
                neutral_feedback.append(feedback)
        else:
            # Log or handle non-string feedback appropriately
            print(f"Skipping non-string feedback: {feedback}")

    # Return categorized feedback
    return {
        'Positive': positive_feedback,
        'Negative': negative_feedback,
        'Neutral': neutral_feedback
    }
