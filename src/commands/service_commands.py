from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

def services(update: Update, context: CallbackContext):
    # context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

    buttons = [
        [InlineKeyboardButton("خارج سور الجامعة", callback_data="outside")], 
        [InlineKeyboardButton("النظام الجامعي", callback_data="uni_system")],
        [InlineKeyboardButton("معلومات دراسية", callback_data="study")],
        [InlineKeyboardButton("الأسئلة الشائعة", callback_data="FAQ")],
        # [InlineKeyboardButton("", callback_data="services")]

    ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="قائمة الخدمات")

def ser_outside(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="service: outside uni")

def ser_uni_system(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="service: uni system")

def ser_study(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="service: acadimic")

def ser_FAQ(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="service: FAQ")