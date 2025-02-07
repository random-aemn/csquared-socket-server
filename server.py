#!/usr/bin/env python

import asyncio
import datetime
import random
import aiofiles
import json

from websockets.asyncio.server import broadcast, serve

CONNECTIONS = set()
KEY_LIST = list()

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def show_time():
    while True:
        message = datetime.datetime.utcnow().isoformat() + "Z"
        broadcast(CONNECTIONS, message)
        #await asyncio.sleep(random.random() * 2 + 1)
        await asyncio.sleep(1)
        
async def get_time_delayed_data():
    await asyncio.sleep(5)
    async with aiofiles.open("./data/rachel-headers-thin.csv", "r") as HEADERFILE:
        headerString = await HEADERFILE.read()
        KEY_LIST = headerString.split(",")
        broadcast(CONNECTIONS, str(KEY_LIST))
        HEADERFILE.close
        
        
    async with aiofiles.open('./data/rachel-thin.csv') as DATAFILE:
        async for line in DATAFILE:
            value_list = line.split(",")
            json_data = dict(zip(KEY_LIST, value_list))
            broadcast(CONNECTIONS, json.dumps(json_data))
            await asyncio.sleep(1)
            

async def main():
    async with serve(register, "localhost", 5678):
        # await show_time()
        await get_time_delayed_data()

if __name__ == "__main__":
    asyncio.run(main())