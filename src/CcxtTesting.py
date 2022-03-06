import ccxt
from models.OHLCV import OHLCV


class CcxtTesting:
    OHLCVS = []

    def run(self):
        ftx = ccxt.ftx()

        markets = ftx.load_markets()

        exchange = 'FTX'
        symbol = 'BTC/USD'
        timeframe = '15m'

        ohlcvs = ftx.fetch_ohlcv(symbol, timeframe=timeframe)

        for ohlcv in ohlcvs:
            timestamp = ohlcv[0]
            open = ohlcv[1]
            high = ohlcv[2]
            low = ohlcv[3]
            close = ohlcv[4]
            volume = ohlcv[5]

            self.OHLCVS.append(
                OHLCV(
                    exchange=exchange,
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
        