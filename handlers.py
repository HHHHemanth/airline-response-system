import csv
import pandas as pd
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from ml_model import get_response, store_message, evaluate_accuracy
from sklearn.metrics import accuracy_score

# Initialize a dictionary to manage user states
user_states = {}

async def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    user_id = update.message.from_user.id
    user_states[user_id] = 'waiting_for_query'
    await update.message.reply_text('👋 Hello! I am your friendly bot. Send me a message and I will respond. 😊')

async def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle incoming messages from users."""
    user_id = update.message.from_user.id
    user_message = update.message.text

    if user_id not in user_states:
        user_states[user_id] = 'waiting_for_query'

    if user_states[user_id] == 'waiting_for_query':
        response = get_response(user_message)  # Get response from ML model
        store_message(user_message, response)
        user_states[user_id] = 'waiting_for_continue'
        
        keyboard = [
            [InlineKeyboardButton("👍 Yes", callback_data='yes')],
            [InlineKeyboardButton("👋 No", callback_data='no')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(response + "\n\nDo you want to continue the conversation?", reply_markup=reply_markup)
    elif user_states[user_id] == 'waiting_for_feedback':
        await handle_feedback(update, context)  # Call the feedback handling function
    else:
        await update.message.reply_text('I didn’t understand that. Please reply with the button options provided.')
# def evaluate_accuracy():
#     # Transform test queries into vectors
#     query_vectors_test = vectorizer.transform(queries_test)
    
#     # Predict responses for the test queries
#     predicted_responses = []
#     for vector in query_vectors_test:
#         distance, index = model.kneighbors(vector)
#         predicted_responses.append(responses_train[index[0][0]])
    
#     # Calculate accuracy score
#     accuracy = accuracy_score(responses_test, predicted_responses)
    
#     # Print accuracy score
#     print(f"Accuracy Score: {accuracy:.4f}")

# Call evaluate_accuracy() to see the accuracy score
evaluate_accuracy()
async def handle_feedback(update: Update, context: CallbackContext) -> None:
    """Handle user feedback."""
    user_id = update.message.from_user.id
    user_message = update.message.text

    if user_id in user_states and user_states[user_id] == 'waiting_for_feedback':
        try:
            # Save feedback to CSV
            with open('feedback.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                # Write both columns initially
                writer.writerow([user_message, user_message])

            # Update the CSV file to ensure the second column has the feedback
            update_feedback_csv('feedback.csv')

            # Send thank you message
            await update.message.reply_text(
                '🙏 Thank you for your feedback! We appreciate your input. \n\n'
                'Visit our website for more information: Global Airways(https://GloablAirways.com) \n'
                'Feel free to reach out if you need further assistance. 😊'
            )

            # Reset state to waiting for query
            user_states[user_id] = 'waiting_for_query'
            await update.message.reply_text('👍 You can now send me another message if you need further assistance.')
        except Exception as e:
            print(f"Error saving feedback: {e}")
            await update.message.reply_text("There was an error saving your feedback.(Please do not include emojis) Please try again.")
    else:
        await update.message.reply_text("It seems there's an issue with your request. Please start a new conversation.")
        user_states[user_id] = 'waiting_for_query'

async def button(update: Update, context: CallbackContext) -> None:
    """Handle button clicks."""
    query = update.callback_query
    user_id = query.from_user.id
    choice = query.data

    if choice == 'yes':
        user_states[user_id] = 'waiting_for_query'
        await query.edit_message_text('👍 Great! Send me another message when you are ready.')
    elif choice == 'no':
        user_states[user_id] = 'waiting_for_feedback'
        await query.edit_message_text('🌟 Please provide your feedback, as this helps our website to grow. 😊')
    else:
        await query.edit_message_text('I didn’t understand that. Please try again.')

def update_feedback_csv(file_path):
    """Update CSV file to ensure the second column has the feedback if it is empty."""
    try:
        # Read the existing CSV file
        df = pd.read_csv(file_path, header=None)
        
        # Ensure there are at least two columns
        if df.shape[1] < 2:
            raise ValueError("CSV file must contain at least two columns")

        # Update rows where the second column is empty
        df[1] = df.apply(lambda row: row[0] if pd.isna(row[1]) else row[1], axis=1)
        
        # Save the updated DataFrame back to the CSV file
        df.to_csv(file_path, index=False, header=False)
        print(f"Updated CSV file: {file_path}")
    except Exception as e:
        print(f"Error updating CSV file: {e}")

