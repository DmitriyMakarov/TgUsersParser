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
    users = [{}]
    iters = client.get_participants(channel)
    for iter in await iters:
        print(iter.to_json())
        users.append(iter.to_json())
        counter = counter + 1
    print(counter)
    xlsx.do_xlsx(users)
    #await client(LeaveChannelRequest(channel))

with client:
    client.loop.run_until_complete(get_user())