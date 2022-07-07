from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, declarative_base
from models.Candle import Candle


class DbController:

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)

        session = sessionmaker(bind=self.engine)
        self.session = session()

        base = declarative_base()
        base.metadata.create_all(self.engine)

    def add_candle(self, Candle):
        Candle.prepare()
        self.session.add(Candle)

    def get_candles(self):
        candles = []
        for candle in self.session.execute(select(Candle)):
            candles.append(candle)

        return candles

    def commit(self):
        self.session.commit()
