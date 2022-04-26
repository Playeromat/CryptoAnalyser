import ccxt
from models.OHLCV import OHLCV


class FtxController:
    OHLCVS = []

    def __init__(self):
        self.ftx = ccxt.ftx()
        self.markets = self.ftx.load_markets()
        self.exchange = 'FTX'
        self.timeframes = self.ftx.timeframes

    def fetch_data(self, symbol, timeframe):
        ohlcvs = self.ftx.fetch_ohlcv(symbol, timeframe=timeframe)

        for ohlcv in ohlcvs:
            timestamp = ohlcv[0]
            open = ohlcv[1]
            high = ohlcv[2]
            low = ohlcv[3]
            close = ohlcv[4]
            volume = ohlcv[5]

            self.OHLCVS.append(
                OHLCV(
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
