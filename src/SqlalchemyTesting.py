import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class SqlalchemyTesting:

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # def create_table(self):
    #     Base = declarative_base()
    #
    #
    #     Base.metadata.create_all(self.engine)

    def add_ohlcv(self, OHLCV):
        from models.Exchange import Exchange
        exchange = Exchange(
            id=OHLCV.id,
            exchange=OHLCV.exchange,
            symbol=OHLCV.symbol,
            timeframe=OHLCV.timeframe,
            timestamp=OHLCV.timestamp,
            open=OHLCV.open,
            high=OHLCV.high,
            low=OHLCV.low,
            close=OHLCV.close,
            volume=OHLCV.volume,
        )

        self.session.add(exchange)

    def commit(self):
        self.session.commit()
