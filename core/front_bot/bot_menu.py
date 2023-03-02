from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


def send_welcome():
    info_button = KeyboardButton('Info')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(info_button)

    return keyboard