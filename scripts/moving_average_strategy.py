import os
import time
import pandas as pd
from binance.client import Client
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET


class BinanceTrader:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)

    def fetch_candle_data(self, symbol, interval):
        candles = self.client.get_klines(symbol=symbol, interval=interval, limit=1000)
        df = pd.DataFrame(candles, columns=[
            'tempo_abertura', 'abertura', 'maxima', 'minima', 'fechamento', 'volume',
            'tempo_fechamento', 'moedas_negociadas', 'numero_trades',
            'volume_ativo_base_compra', 'volume_ativo_cotacao', '-'
        ])
        df = df[['fechamento', 'tempo_fechamento', 'volume']].astype(float)
        df['tempo_fechamento'] = pd.to_datetime(df['tempo_fechamento'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')
        return df

    def get_account_balance(self, asset):
        account = self.client.get_account()
        for balance in account['balances']:
            if balance['asset'] == asset:
                return float(balance['free'])
        return 0.0

    def place_order(self, symbol, side, quantity):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )


class MovingAverageStrategy:
    def __init__(self, trader, symbol, interval, quantity):
        self.trader = trader
        self.symbol = symbol
        self.interval = interval
        self.quantity = quantity
        self.position = False

    def execute(self):
        data = self.trader.fetch_candle_data(self.symbol, self.interval)
        data['fast_average'] = data['fechamento'].rolling(window=7).mean()
        data['slow_average'] = data['fechamento'].rolling(window=40).mean()

        last_fast_avg = data['fast_average'].iloc[-1]
        last_slow_avg = data['slow_average'].iloc[-1]

        print(f'Última média rápida: {last_fast_avg} | Última média lenta: {last_slow_avg}')

        balance = self.trader.get_account_balance(self.symbol.replace('USDT', ''))
        if last_fast_avg > last_slow_avg and not self.position:

            self.trader.place_order(self.symbol, SIDE_BUY, self.quantity)
            
            print("Comprou o ativo")
            self.position = True

        elif last_fast_avg < last_slow_avg and self.position:

            self.trader.place_order(self.symbol, SIDE_SELL, self.quantity)
            
            print("Vendeu o ativo")
            self.position = False
