#!/usr/bin/env python

import asyncio
import datetime
import random
import aiofiles
import json
import sys

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
    headerFileName = sys.argv[1] + '-headers.csv'
    async with aiofiles.open(headerFileName, "r") as HEADERFILE:
        headerString = await HEADERFILE.read()
        KEY_LIST = headerString.strip().split(",")
        #broadcast(CONNECTIONS, str(KEY_LIST))
        HEADERFILE.close
        
    dataFiileName = sys.argv[1] + '.csv'
    async with aiofiles.open(dataFiileName) as DATAFILE:
        async for line in DATAFILE:
            value_list = line.strip().split(",")
            json_data = dict(zip(KEY_LIST, value_list))
            broadcast(CONNECTIONS, json.dumps(json_data))
            await asyncio.sleep(1)
            

async def main():
    if len(sys.argv) < 3:
        host = "127.0.0.1"
    else:
        host = "0.0.0.0"
        
    async with serve(register, host, 5678):
        # await show_time()
        await get_time_delayed_data()

if __name__ == "__main__":
    asyncio.run(main())