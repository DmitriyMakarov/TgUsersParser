from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import asyncio
import configparser
from core.front_bot import bot_menu
from res.strings import bot_messages
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from core.helpers import mysql


config = configparser.ConfigParser()
config.read('../../res/config/config.ini')
config.sections()


apy_key = config['TG']['api_key']
print(apy_key)


bot = Bot(token=apy_key)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class States(Helper):
    mode = HelperMode.snake_case
    LINK_STATE_0 = ListItem() #ждем ссылку

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    print(message.chat.id)
    #print(await users_db.user_exist_check(message.chat.id))
    print(asyncio.run(mysql.check_user_exist(message.chat.id)), 'test')
    #print(DB.user_exist_check(user_id=str(message.chat.id)))
#    if await users_db.user_exist_check(message.chat.id) == 400:
#        users_db.user_add(message.chat.id)
    keyboard = bot_menu.send_welcome()
    await message.answer(bot_messages.start_message, reply_markup=keyboard)


@dp.message_handler(state='*', commands=['getusers'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply('no argument')

    if (not argument.isdigit()) or (not int(argument) < len(States.all())):
        return await message.reply('key no'.format(key=argument))

    await state.set_state(States.all()[int(argument)])
    await message.reply('state change', reply=False)


@dp.message_handler(state=States.LINK_STATE_0)
async def first_test_state_case_met(message: types.Message):
    await message.reply('Первый!', reply=False)
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()

@dp.message_handler()
async def cmd_start(message: types.Message):
    print(message.text)
    if message.text == 'Меню ℹ️':
        keyboard = bot_menu.main_menu()
        await message.answer('menu', reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':

    asyncio.run(main())