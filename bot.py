import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from handlers import start, handle_message, handle_feedback, button
from config import BOT_TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Handle /start command
    application.add_handler(CommandHandler('start', start))

    # Handle any text message
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Handle button presses
    application.add_handler(CallbackQueryHandler(button))

    # Handle user feedback
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_feedback))

    logger.info('Bot is starting...')
    application.run_polling()

if __name__ == '__main__':
    main()
