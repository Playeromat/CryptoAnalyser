import sqlalchemy
import hashlib

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class OHLCV(Base):
    __tablename__ = 'ftx'
    id = sqlalchemy.Column(sqlalchemy.INT, primary_key=True, unique=True, autoincrement=True, index=True)
    hash = sqlalchemy.Column(sqlalchemy.String(length=100), unique=True)
    exchange = sqlalchemy.Column(sqlalchemy.String(length=100))
    symbol = sqlalchemy.Column(sqlalchemy.String(length=100))
    timeframe = sqlalchemy.Column(sqlalchemy.String(length=100))
    open = sqlalchemy.Column(sqlalchemy.Float)
    high = sqlalchemy.Column(sqlalchemy.Float)
    low = sqlalchemy.Column(sqlalchemy.Float)
    close = sqlalchemy.Column(sqlalchemy.Float)
    volume = sqlalchemy.Column(sqlalchemy.Float)
    volatility = sqlalchemy.Column(sqlalchemy.Float)
    candle_size = sqlalchemy.Column(sqlalchemy.Float)
    timestamp = sqlalchemy.Column(sqlalchemy.BIGINT)
    time_readable = sqlalchemy.Column(sqlalchemy.String(length=100))

    def prepare(self):
        hash_string = self.exchange + self.symbol + self.timeframe + str(self.timestamp)
        self.hash = hashlib.md5(hash_string.encode()).hexdigest()

        self.volatility = abs(self.high - self.low)
        self.candle_size = abs(self.close - self.open)
        self.time_readable = datetime.utcfromtimestamp(self.timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


Base.metadata.create_all(
    create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)
)
