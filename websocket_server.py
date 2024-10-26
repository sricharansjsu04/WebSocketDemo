import asyncio
from random import randint
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        modified_message = f"{message} [{randint(1, 100)}]"
        await websocket.send(modified_message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
