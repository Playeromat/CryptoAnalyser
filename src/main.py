from CcxtTesting import CcxtTesting
from SqlalchemyTesting import SqlalchemyTesting
from UserInterface import UserInterface

ccxt_testing = CcxtTesting()
sqlalchemy_testing = SqlalchemyTesting()
user_interface = UserInterface()

# sqlalchemy_testing.create_table()

markets = [*ccxt_testing.get_markets()]
timeframes = [*ccxt_testing.get_timeframes()]

# user_input_markets = (3, 6)
# user_input_timeframes = (4, 9)

user_input_markets = user_interface.multi_select(markets)
user_input_timeframes = user_interface.multi_select(timeframes)

for user_input_market in user_input_markets:
   for user_input_timeframe in user_input_timeframes:
       ccxt_testing.fetch_data(markets[user_input_market], timeframes[user_input_timeframe])


for OHLCV in ccxt_testing.OHLCVS:
    sqlalchemy_testing.add_ohlcv(OHLCV)

sqlalchemy_testing.commit()
