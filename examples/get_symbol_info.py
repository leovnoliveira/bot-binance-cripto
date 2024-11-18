from binance.client import Client
import os

api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')

cliente_binance = Client(api_key, api_secret, testnet=True)

symbol_info = cliente_binance.get_symbol_info('ETHBRL')
lot_size_filter = next(f for f in symbol_info['filters'] if f['filterType'] == 'LOT_SIZE')
min_qty = float(lot_size_filter['minQty'])
max_qty = float(lot_size_filter['maxQty'])
step_size = float(lot_size_filter['stepSize'])

print(lot_size_filter, min_qty, max_qty, step_size)
