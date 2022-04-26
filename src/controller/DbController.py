import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, declarative_base
from models.OHLCV import OHLCV


class DbController:

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)

        session = sessionmaker(bind=self.engine)
        self.session = session()

        base = declarative_base()
        base.metadata.create_all(self.engine)

    def add_ohlcv(self, OHLCV):
        OHLCV.prepare()
        self.session.add(OHLCV)

    def get_ohlcvs(self):
        ohlcvs = []
        for ohlcv in self.session.execute(select(OHLCV)):
            ohlcvs.append(ohlcv)

        return ohlcvs

    def commit(self):
        self.session.commit()
