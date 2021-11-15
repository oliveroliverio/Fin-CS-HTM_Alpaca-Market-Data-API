import websocket, json
from config import *

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": config.API_KEY, "secret_key": config.SECRET_KEY}
    }
    ws.send(json.dumps(auth_data))

#     channel_data = {
#         "action": "subscribe",
#         "params": TICKERS
#     }

#     ws.send(json.dumps(channel_data))


def on_message(ws, message):
    print("received a message")
    print(message)

# def on_close(ws):
#     print("closed connection")

socket = "wss://data.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket, on_open=on_open)
ws.run_forever()