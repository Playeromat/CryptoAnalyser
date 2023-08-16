import hashlib

from datetime import datetime

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

Base = declarative_base()


class Candle(Base):
    __tablename__ = 'binance'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    hash = Column(String(length=100), unique=True)
    exchange = Column(String(length=100))
    symbol = Column(String(length=100))
    timeframe = Column(String(length=100))
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    volatility = Column(Float)
    candle_size = Column(Float)
    timestamp = Column(Float)
    time_readable = Column(DateTime)

    def prepare(self):
        hash_string = self.exchange + self.symbol + self.timeframe + str(self.timestamp)
        self.hash = hashlib.md5(hash_string.encode()).hexdigest()

        self.volatility = abs(self.high - self.low)
        self.candle_size = abs(self.close - self.open)
        self.time_readable = datetime.utcfromtimestamp(self.timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


Base.metadata.create_all(
    create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)
)
