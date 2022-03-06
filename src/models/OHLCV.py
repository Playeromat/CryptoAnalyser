import hashlib


class OHLCV:

    def __init__(self, exchange, symbol, timeframe, timestamp, open, high, low, close, volume):
        self.exchange = exchange
        self.symbol = symbol
        self.timeframe = timeframe
        self.timestamp = timestamp
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

        hash_string = exchange + symbol + timeframe + str(timestamp)

        self.id = hashlib.md5(hash_string.encode()).hexdigest()
