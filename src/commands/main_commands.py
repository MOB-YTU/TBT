from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from data.Messages import *

def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

def about_bot(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=about_message)

def about_union(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=about_message)
