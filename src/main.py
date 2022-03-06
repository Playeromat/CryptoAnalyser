from CcxtTesting import CcxtTesting
from SqlalchemyTesting import SqlalchemyTesting

ccxt_testing = CcxtTesting()
sqlalchemy_testing = SqlalchemyTesting()

# sqlalchemy_testing.create_table()

ccxt_testing.run()

for OHLCV in ccxt_testing.OHLCVS:
    sqlalchemy_testing.add_ohlcv(OHLCV)

sqlalchemy_testing.commit()
