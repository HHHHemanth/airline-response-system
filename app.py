from flask import Flask, jsonify, render_template
from ml_model import analyze_sentiments

app = Flask(__name__)

# Path to your feedback CSV
FEEDBACK_FILE_PATH = 'feedback.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sentiment_data')
def sentiment_data():
    sentiment_results = analyze_sentiments(FEEDBACK_FILE_PATH)
    return jsonify(sentiment_results)

if __name__ == '__main__':
    app.run(debug=True)
