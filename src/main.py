from dotenv import load_dotenv
load_dotenv()
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from flask import Flask, request

from commands.main_commands import about_bot, about_union, help
from commands.service_commands import ser_FAQ, ser_outside, ser_study, ser_uni_system, services

from data.Messages import *


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# Define your bot token
TOKEN = os.getenv('BOT_TOKEN', '5978309881:AAFXZe5x_GLL2xz-BEHzPR-J5QAECXuQZ9A')

# Initialize the updater and dispatcher
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define start command handlers
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

    buttons = [
        [InlineKeyboardButton("مساعدة", callback_data="help")], 
        [InlineKeyboardButton("عن البوت", callback_data="about_bot")],
        [InlineKeyboardButton("خدمات البوت", callback_data="services")],
        [InlineKeyboardButton("عن الاتحاد", callback_data="abot_union")],

    ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="<================= اختر من القائمة الآتية👇 ==================>")

# Define callback handler
def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    call_back_dict = {
        'help': help,
        'about_bot': about_bot,
        'services': services,
        'abot_union': about_union,
        'outside': ser_outside,
        'uni_system': ser_uni_system,
        'study': ser_study,
        'FAQ': ser_FAQ
    }

    # Handle the specific command based on callback data
    call_back_dict[query.data](update, context)
    # if query.data == 'help':
    #     help(update,context)
    # elif query.data == 'about_bot':
    #     about_bot(update,context)
    # elif query.data == 'services':
    #     services(update,context)
    # elif query.data == 'abot_union':
    #     about_union(update,context)
    
    # elif query.data == 'outside':
    #     ser_outside(update,context)
    # elif query.data == 'uni_system':
    #     ser_uni_system(update,context)
    # elif query.data == 'study':
    #     ser_study(update,context)
    # elif query.data == 'FAQ':
    #     ser_FAQ(update,context)

def main():
    callback_handler = CallbackQueryHandler(button_callback)
    dispatcher.add_handler(callback_handler)

    # Command Handlers
    command_func = { # main commands
        'start': start,
        'help': help,
        'about': about_bot
    }
    # for k in command_func:
    #     handler = CommandHandler(k, command_func[k])
    #     dispatcher.add_handler(handler)

    for k, v in command_func.items():
        handler = CommandHandler(k, v)
        dispatcher.add_handler(handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C to stop it
    updater.idle()

app = Flask(__name__)

# Set up a basic route to handle incoming requests from Cloud Run
@app.route('/', methods=['POST'])
def webhook():
    json_data = request.get_json()
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    main()