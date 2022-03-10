import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class SqlalchemyTesting:

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://crypto_analyser:crypto_analyser@crypto_analyser_mariadb:3306/crypto_analyser", echo=True, future=True)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        Base = declarative_base()
        Base.metadata.create_all(self.engine)

    def add_ohlcv(self, OHLCV):
        OHLCV.prepare()
        self.session.add(OHLCV)

    def commit(self):
        self.session.commit()
