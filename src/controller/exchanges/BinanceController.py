import ccxt
from models.Candle import Candle


class BinanceController:
    candles = []

    def __init__(self):
        self.binance = ccxt.binance()
        self.markets = self.binance.load_markets()
        self.exchange = 'Binance'
        self.timeframes = self.binance.timeframes

    def fetch_data(self, symbol, timeframe):
        candles = self.binance.fetch_ohlcv(symbol, timeframe=timeframe)

        for candle in candles:
            timestamp = candle[0]
            open = candle[1]
            high = candle[2]
            low = candle[3]
            close = candle[4]
            volume = candle[5]

            self.candles.append(
                Candle(
                    exchange=self.exchange,
                    symbol=symbol,
                    timeframe=timeframe,
                    timestamp=timestamp,
                    open=open,
                    high=high,
                    low=low,
                    close=close,
                    volume=volume
                )
            )

    def get_markets(self):
        return self.markets

    def get_timeframes(self):
        return self.timeframes
