import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Exchange(Base):
    __tablename__ = 'ftx'
    id = sqlalchemy.Column(sqlalchemy.String(length=100), primary_key=True)
    exchange = sqlalchemy.Column(sqlalchemy.String(length=100))
    symbol = sqlalchemy.Column(sqlalchemy.String(length=100))
    timeframe = sqlalchemy.Column(sqlalchemy.String(length=100))
    timestamp = sqlalchemy.Column(sqlalchemy.BIGINT)
    open = sqlalchemy.Column(sqlalchemy.Float)
    high = sqlalchemy.Column(sqlalchemy.Float)
    low = sqlalchemy.Column(sqlalchemy.Float)
    close = sqlalchemy.Column(sqlalchemy.Float)
    volume = sqlalchemy.Column(sqlalchemy.Float)


Base.metadata.create_all(
    create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)
)
