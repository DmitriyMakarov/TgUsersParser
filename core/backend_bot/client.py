from telethon import TelegramClient, utils
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
import asyncio
import configparser
import datetime

from core.xlsx import xlsx


config = configparser.ConfigParser()
config.read('../../res/config/config.ini')
config.sections()

api_id = config['TG Client']['api_id']
api_hash = config['TG Client']['api_hash']
session_file = '../../res/config/client'

client = TelegramClient(session_file, api_id, api_hash)

async def main():
    me = await client.get_me()
    print(me.to_json())

async def get_user():
    channel = 'https://t.me/drgrtdeeww'
    counter = 0
    iters = client.get_participants(channel)
    users = dict()
    for iter in await iters:
        user = {'id': iter.id, 'bot': iter.bot, 'premium': iter.premium, 'access_hash': str(iter.access_hash),
                'first_name': iter.first_name, 'last_name': iter.last_name, 'username': iter.username,
                'phone': iter.phone, 'status': str(iter.status) }
        users.update({counter: user})
        counter = counter + 1

    xlsx.do('111111', datetime.datetime.now().strftime('%d-%m_%H-%M'), 'чат', users)


with client:
    client.loop.run_until_complete(get_user())