import hashlib

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float

Base = declarative_base()


class WeekAnalysis(Base):
    __tablename__ = 'week_analysis'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    hash = Column(String(length=100), unique=True)
    exchange = Column(String(length=100))
    symbol = Column(String(length=100))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    weekly_high = Column(Float)
    weekly_low = Column(Float)
    weekday_high = Column(String(length=16))
    weekday_low = Column(String(length=16))
    weekday_range_high = Column(String(length=16))
    weekday_range_low = Column(String(length=16))
    trend = Column(String(length=16))

    def prepare(self):
        hash_string = self.exchange + self.symbol + str(self.start_date)
        self.hash = hashlib.md5(hash_string.encode()).hexdigest()


Base.metadata.create_all(
    create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)
)
