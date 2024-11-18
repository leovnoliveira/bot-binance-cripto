import os
from binance.client import Client
from binance.enums import SIDE_BUY, ORDER_TYPE_MARKET

api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

cliente_binance = Client(api_key, api_secret, testnet=True)

order = cliente_binance.create_order(
    symbol='SOLBRL',
    side=SIDE_BUY,
    type=ORDER_TYPE_MARKET,
    quantity=0.015,
)

print(order)
