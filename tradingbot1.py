from http.client import ImproperConnectionState
import pandas as pd 
Import sqlalchemy
from binance.client import Client
from binance import binanceSocketManager

client = Client(api_key,api_secret)
bsm = binanceSocketManager(client)
socket = bsm.trade_socket('BTCUSDT') # Crypto Ticket Symbol

await socket._aenter_()
msg = await socket.recv()
print(msg)