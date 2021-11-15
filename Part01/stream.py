import websocket, json
from config import *

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": config.API_KEY, "secret_key": config.SECRET_KEY}
    }
    # send auth data to alpaca
    ws.send(json.dumps(auth_data))
    # create listen_message object that youll send to alpaca
    listen_message = {"action": "listen", "data": {"streams": ["T.SPY"]}}
    # send listen_message to alpaca, which will send back stream data
    ws.send(json.dumps(listen_message))
def on_message(ws, message):
    print("received a message")
    print(message)

# def on_close(ws):
#     print("closed connection")

socket = "wss://data.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()