import os
import time
from moving_average_strategy import BinanceTrader, MovingAverageStrategy

if __name__ == '__main__':
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('SECRET_KEY')

    trader = BinanceTrader(api_key, api_secret)
    strategy = MovingAverageStrategy(trader, symbol='SOLUSDT', interval=Client.KLINE_INTERVAL_1HOUR, quantity=0.015)

    while True:
        strategy.execute()
        time.sleep(60 * 60)
