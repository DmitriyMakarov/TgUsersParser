from telethon import TelegramClient, utils
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
import asyncio
import configparser

from core.xlsx import xlsx


config = configparser.ConfigParser()
config.read('../../res/config/config.ini')
config.sections()

api_id = config['TG Client']['api_id']
api_hash = config['TG Client']['api_hash']
session_file = '../../res/config/client'

client = TelegramClient(session_file, api_id, api_hash)

async def main():
    # Now you can use all client methods listed below, like for example...
    me = await client.get_me()
    print(me.to_json())

async def get_user():
    channel = 'https://t.me/drgrtdeeww'
   # await client(JoinChannelRequest(channel))
    #await participants = client.get_participants(channel)
   # await print(client.get_participants(channel))
    counter = 0
    iters = client.get_participants(channel)
    users = dict()
    for iter in await iters:
        user = {'id': iter.id, 'bot': iter.bot, 'premium': iter.premium, 'access_hash': iter.access_hash,
                'first_name': iter.first_name, 'last_name': iter.last_name, 'username': iter.username,
                'phone': iter.phone, 'status': str(iter.status) }
        print(user)

        users.update({counter: user})

        counter = counter + 1
        #print(user)
    #print(users)
    xlsx.do(users)
        #for key in user.keys():
        #    user[key]=iter.key
        #    #users.update(user)
        #    print(key)
    #    counter = counter + 1
    #print(users)
    #print(counter)
    #xlsx.do_xlsx(users)
    #await client(LeaveChannelRequest(channel))

with client:
    client.loop.run_until_complete(get_user())