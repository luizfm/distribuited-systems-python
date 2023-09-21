import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(f"Server received: {message}")

server = websockets.serve(echo, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()