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
wscat -c wss://paper-api.alpaca.markets/stream
```