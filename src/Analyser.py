from controller.exchanges.FtxController import FtxController
from controller.DbController import DbController
from UserInterface import UserInterface


class Analyser:

    def __init__(self):
        self.ftx_controller = FtxController()
        self.db_controller = DbController()
        self.user_interface = UserInterface()

    def run(self):
        markets = [*self.ftx_controller.get_markets()]
        timeframes = [*self.ftx_controller.get_timeframes()]

        user_input_markets = self.user_interface.multi_select(markets)
        user_input_timeframes = self.user_interface.multi_select(timeframes)

        for user_input_market in user_input_markets:
            for user_input_timeframe in user_input_timeframes:
                self.ftx_controller.fetch_data(markets[user_input_market], timeframes[user_input_timeframe])

        for candle in self.ftx_controller.candles:
            self.db_controller.add_candle(candle)

        self.db_controller.commit()
