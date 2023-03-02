from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import asyncio
import configparser
from core.front_bot import bot_menu


config = configparser.ConfigParser()
config.read('../../res/config/config.ini')
config.sections()

apy_key = config['TG']['api_key']
print(apy_key)


bot = Bot(token=apy_key)

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    keyboard = bot_menu.send_welcome()
    await message.answer("Hello!", reply_markup=keyboard)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':

    asyncio.run(main())