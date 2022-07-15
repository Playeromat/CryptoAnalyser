from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, declarative_base
from models.Candle import Candle
import sqlalchemy


class DbController:

    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True,
            future=True)

        session = sessionmaker(bind=self.engine)
        self.session = session()

        base = declarative_base()
        base.metadata.create_all(self.engine)

    # TODO: On duplicate key Update
    def add_entry(self, entry):
        entry.prepare()
        self.session.add(entry)

    def get_candles(self, exchange=None, symbol=None, timeframe=None):
        query = self.session.query(Candle)

        if exchange is not None:
            query = query.filter(Candle.exchange == exchange)

        if symbol is not None:
            query = query.filter(Candle.symbol == symbol)

        if timeframe is not None:
            query = query.filter(Candle.timeframe == timeframe)

        return query.all()

    def commit(self):
        self.session.commit()
