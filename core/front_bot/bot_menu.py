from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def send_welcome():
    info_button = KeyboardButton('Меню ℹ️')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(info_button)

    return keyboard

def main_menu():
    balance_inline_button = InlineKeyboardButton('Баланс 💵', callback_data='balance')
    payment_inline_button = InlineKeyboardButton('Оплата 🛒', callback_data='payment')
    help_inline_button = InlineKeyboardButton('Помощь 🆘', callback_data='help')
    work_inline_button = InlineKeyboardButton('Спарсить пользователей ', switch_inline_query_current_chat='parse: ')
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(balance_inline_button, payment_inline_button)
    inline_keyboard.add(help_inline_button)
    inline_keyboard.add(work_inline_button)
    return inline_keyboard