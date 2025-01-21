import asyncio
import websockets
import orjson

BASE_URL = "wss://fstream.binance.com/ws"
STREAM_NAME = "btcusdt@aggTrade"

request = {
    "method": "SUBSCRIBE",
    "params": [STREAM_NAME],
    "id": 1,
}


async def connect_to_stream():
    uri = f"{BASE_URL}/{STREAM_NAME}"
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")
        while True:
            try:
                await websocket.send(orjson.dumps(request))
                response = await websocket.recv()
                print(f"Received data: {response}")

                # Implement your trend-following logic here
                # Example: Check if the price is above/below a moving average
                # and place trades accordingly

            except websockets.ConnectionClosed:
                print("Connection closed")
                break


async def main():
    while True:
        try:
            await connect_to_stream()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
