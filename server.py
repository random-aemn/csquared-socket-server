#!/usr/bin/env python

import asyncio
from datetime import datetime, timedelta
import random
import aiofiles
import json
import sys
from itertools import islice
import argparse


from websockets.asyncio.server import broadcast, serve

CONNECTIONS = set()
KEY_LIST = list()
BATCH_SIZE = 9


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
        
async def get_time_delayed_data(headerFileName, dataFileName, in_sleeptime):
    await asyncio.sleep(5)
    # headerFileName = sys.argv[1] + '-headers.csv'

    async with aiofiles.open(headerFileName, "r") as HEADERFILE:
        headerString = await HEADERFILE.read()
        KEY_LIST = headerString.strip().split(",")
        #broadcast(CONNECTIONS, str(KEY_LIST))
        HEADERFILE.close

    # dataFileName = sys.argv[1] + '.csv'
    # allocate necessary variables
    one_second = timedelta(seconds=1)
    json_array = []
    firstPass = True
    REPORT_DATE_INDEX = 1
    sentinelDate = None

    async with aiofiles.open(dataFileName) as DATAFILE:
        async for line in DATAFILE:

            line = str(line)
            value_list = line.strip().split(",")
            json_data = dict(zip(KEY_LIST, value_list))

            if firstPass:
                sentinelDate = datetime.fromisoformat(value_list[REPORT_DATE_INDEX])
                json_array.append(json_data)
                # sentinelDate = sentinelDate + one_second
                firstPass = False
       
            else:
                recordDate = datetime.fromisoformat(value_list[REPORT_DATE_INDEX])
                if recordDate != sentinelDate:
                    # New position report date found in data; publish the current list; clear the publication list
                    # and add the most recent record to the publication list
                    broadcast(CONNECTIONS, json.dumps(json_array))
                    # sentinelDate = sentinelDate + one_second
                    json_array = []
                    while sentinelDate < recordDate:
                        # Simulate the time delay between position reports
                        sentinelDate = sentinelDate + one_second
                        await asyncio.sleep(in_sleeptime)  
                    json_array.append(json_data)
                    
                else:
                    # Add current record to the publication list
                    json_array.append(json_data)
        broadcast(CONNECTIONS, json.dumps(json_array))

async def print_args(data):
    print(data, flush=True)        


async def main():
    
    parser = argparse.ArgumentParser()
# This creates a mandatory positional argument
    parser.add_argument('headerfilename', help='The file defining column headers.')
    parser.add_argument('datafilename', help='The file containing the data matching the info in the header file.')
    parser.add_argument("-b", "--bindAddress", default='127.0.0.1', help="Network interface bind address ")
    parser.add_argument("-s", "--sleeptime", type=float, default=1, help="""Number of seconds to wait between each iteration of the read loop.  
                        A value  0 < sleeptime < 1 will decrease the wait time between loop iterations.""")
    args = parser.parse_args()
    # "127.0.0.1" (or "localhost"): Restricts connections exclusively to the local machine. 
    # External devices on your network cannot connect to it.
    # "0.0.0.0" (or ""): Binds to all available network interfaces. 
    # This allows any machine on your local network (or the internet, if port-forwarded) to connect using your computer's 
    # local IP address.
    # Specific Local IP (e.g., "192.168.1.5"): Restricts the server to accept connections arriving only on 
    # that specific network card or interface.
    # if len(sys.argv) < 3:
    #     host = "127.0.0.1"
    # else:
    #     host = "0.0.0.0"
    await print_args (args)
        
    async with serve(register, args.bindAddress, 5678):
        # await show_time()
        await get_time_delayed_data(args.headerfilename, args.datafilename, args.sleeptime)

if __name__ == "__main__":
    asyncio.run(main())