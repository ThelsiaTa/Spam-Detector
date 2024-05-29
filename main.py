from typing import Final
from telegram import Update
import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from spam_classifier import predict_spam_or_ham

TOKEN: Final = '6965949026:AAGZukEZo1RbFQdoaJWnKbF8kCa6p4KMB7Y'
BOT_USERNAME: Final = '@spamieDetect_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Spamie, a spam detector Bot. You could add me in the group chat to remove spam messages or text me the message you think is spam. If not spam then it's ham.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I will automatically delete spam messages.")

# Handle Responses
def handle_response(text: str) -> str:
    if predict_spam_or_ham(text):
        return 'This is a spam message'
    else:
        return 'This is ham'

# Handle Messages
bot = telegram.Bot(token = TOKEN)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    chat_id = update.message.chat_id
    message_id = update.message.message_id

    if update.message.chat.type == 'private':
        # Respond directly to the user in a private chat
        response = handle_response(text)
        await update.message.reply_text(response)
    else:
        # Handle messages in a group chat
        if predict_spam_or_ham(text):
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            response = "The spam message has just been deleted"
            await context.bot.send_message(chat_id=chat_id, text=response)

# Handle Errors
def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Poll the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
