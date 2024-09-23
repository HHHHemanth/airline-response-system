#  Smart Response System for Airline Queries with Machine Learning✈️ 

## 🚀 Project Overview

This project involves the development of a **Smart Response System** designed to handle airline customer service queries using machine learning. It automates responses to common customer inquiries, offering faster and more efficient customer support. The system uses sentiment analysis to classify feedback and provide insights into user sentiment, and it is integrated with Telegram for customer interaction.

## 🛠️ Features
- 🤖 Automated response system for airline queries
- 📊 Sentiment analysis of customer feedback
- 🌐 Flask web framework for real-time interaction
- 🗃️ Preprocessing and classification of airline queries
- 📝 Data storage in CSV format
- 💬 Telegram bot integration for handling queries

## 📁 Project Components
1. **Data Acquisition & Preprocessing**: The dataset consists of airline queries and replies stored in `merged_file.csv`, which is processed using machine learning techniques.
2. **Machine Learning Algorithm**: The system uses text classification to match customer queries with pre-defined responses.
3. **Sentiment Analysis**: Feedback from customers is analyzed using the `TextBlob` library to classify sentiments as positive, negative, or neutral.
4. **Web Interface**: A web-based interface using **Flask** displays sentiment analysis results with graphical representation.
5. **Telegram Integration**: The system is integrated with Telegram to handle real-time customer service requests and provide automated responses.

## 📂 Project Structure
```bash
├── app.py                   # Flask web application entry point
├── ml_model.py               # Machine learning model and 
├── handlers.py
├── bot.py
├── config.py
sentiment analysis code
├── feedback.csv              # CSV file containing customer feedback
├── merged_file.csv           # CSV file containing airline queries and replies
├── static/                   # Static files (CSS, JS, images)
├── templates/                # HTML templates for the Flask web app
└── README.md                 # Project documentation
```



## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/HHHHemanth/airline-response-system
   
   cd airline-response-system
   ```
2. Run the bot:
```bash
   python bot.py
```
3. Run the Flask:
```bash
   python app.py
```
4. Access the web interface at http://127.0.0.1:5000/.

## 📋 Requirements
- 🐍 Python
- 🧰 Flask
- 📜 TextBlob
- 📊 Pandas

You can install the required libraries using:
```bash 
pip install Flask TextBlob pandas
```
## 🤖 Telegram Bot Setup
1. Open Telegram and search for the BotFather.

2. Start a chat with BotFather by clicking the Start button.

3. Use the /newbot command to create a new bot.

4. Follow the instructions to:

- Provide a name for your bot (e.g., "Airline Support Bot").
- Choose a unique username for your bot that ends with "_bot" (e.g., "airline_support_bot").
5. Once created, BotFather will give you a Telegram API Token. Save this token, as you'll need it to connect your bot to the system.

6. In your project directory, create a .env file and add the following line:

``` bash
TELEGRAM_BOT_TOKEN=YOUR_API_TOKEN 
```

Replace YOUR_API_TOKEN with the token provided by BotFather.

7. Add your bot to any Telegram group or chat where it will provide automated airline query responses.
## 🎯 Usage
1. Run the System: Start the Flask application and interact with the system through the Telegram bot or directly through the web interface.
2. Sentiment Analysis: The system will process customer feedback from feedback.csv and display the analysis in a graphical format.

## 🛠️ Future Work
- 🌍 Expand to other social media platforms such as Twitter and Facebook.
- 🧠 Implement advanced NLP techniques for better response accuracy.
- ☁️ Deploy the system on cloud platforms for better scalability.

## 🎯 Goals Checklist
 - ✅Automated response system for queries
 -  ✅Sentiment analysis using TextBlob
 - 🔲Deploy on cloud for scalability
 - 🔲Expand integration with other social platforms

 



