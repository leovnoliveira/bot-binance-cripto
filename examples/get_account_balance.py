from binance.client import Client
import os

api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

cliente_binance = Client(api_key, api_secret, testnet=True)

conta = cliente_binance.get_account()

for cripto in conta['balances']:
    if float(cripto['free']) > 0:
        print(cripto)
