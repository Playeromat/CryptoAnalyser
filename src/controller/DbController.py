from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Candle import Candle


class DbController:

    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=False,
            future=True)

        session = sessionmaker(bind=self.engine)
        self.session = session()

    def add_entries(self, entries):
        for entry in entries:
            self.add_entry(entry)

        self.commit()

    # TODO: On duplicate key Update
    def add_entry(self, entry):
        entry.prepare()

        if self.session.query(type(entry)).filter_by(hash=entry.hash).first() is not None:
            print("Skipped")
            # self.session.execute(update(entry).where(entry.hash == entry.hash).values(
            #     entry.
            # ))
        else:
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
