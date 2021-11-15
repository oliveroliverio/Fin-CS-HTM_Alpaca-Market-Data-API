# Part 01 - Streaming with python and websockets
[documentation](https://alpaca.markets/docs/api-documentation/api-v2/streaming/)
Can stream trades, quotes, and minute bars.  You can listen on this channel and get every single trade executed. You

Goal is to create a websocket connection, then listen on a stream.

First need to authenticate using alpaca API/secret key
```
{
    "action": "authenticate",
    "data": {
        "key_id": "{YOUR_API_KEY_ID}",
        "secret_key": "{YOUR_API_SECRET_KEY}"
    }
}
```

Modify your config.py file to contain the keys

Install `wscat`
```
sudo npm install -g wscat
```

Connect to stream with `wscat`
```
wscat -c wss://api.alpaca.markets/stream
```

Input authentation string

```
{"action": "authenticate", "data": { "key_id": "", "secret_key": ""}}
```
[doc on streaming](https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v1/streaming/)

Install websocket client
```
pip install websocket-client
```

Use this websockets address: `wss://data.alpaca.markets/stream`

Start with basic python app

`stream.py`
```python
def on_open(ws):
    print("opened")

socket = "wss://data.alpaca.markets/stream"
ws = websocket.WebSocketApp(socket, on_open=on_open)
ws.run_forever()
```
Run `python stream.py`.  Works.  Now it's waiting for instructions.
Here we'll pass the authentication info.  Note
```
auth_data = {
    "action": "authenticate",
    "params": API_KEY
}
```

Here we give it an "action" and "parameters"

```python
def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": config.API_KEY, "secret_key": config.SECRET_KEY}
    }
    ws.send(json.dumps(auth_data))
```
we.send sends auth to alpaca.  Note, remember how we get an authentication reply/message after sending this?  Need to handle that somehow.  We'll do it on a on_message() method

```python
def on_message(ws, message):
    print("recieved a message")
    print(message)
```

## Stopped here.  21:02.  Cannot authenticate.  Not recieving any messages