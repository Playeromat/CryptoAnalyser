from controller.exchanges.FtxController import FtxController
from controller.DbController import DbController
from UserInterface import UserInterface

from controller.analyser.WeekAnalyser import WeekAnalyser
from controller.analyser.MonthAnalyser import MonthAnalyser


class Analyser:

    def __init__(self):
        self.ftx_controller = FtxController()
        self.db_controller = DbController()
        self.user_interface = UserInterface()

        self.week_analyser = WeekAnalyser()
        self.month_analyser = MonthAnalyser()

        self.markets = []
        self.timeframes = []

        self.user_input_markets = []
        self.user_input_timeframes = []

    def run(self):
        self.get_user_selections()
        self.get_candle_data()
        self.run_analysis()

    def get_user_selections(self):
        self.markets = [*self.ftx_controller.get_markets()]
        self.timeframes = [*self.ftx_controller.get_timeframes()]

        self.user_input_markets = self.user_interface.multi_select(self.markets)
        self.user_input_timeframes = self.user_interface.multi_select(self.timeframes)

    def get_candle_data(self):
        for user_input_market in self.user_input_markets:
            for user_input_timeframe in self.user_input_timeframes:
                self.ftx_controller.fetch_data(self.markets[user_input_market], self.timeframes[user_input_timeframe])

        self.db_controller.add_entries(self.ftx_controller.candles)

    def run_analysis(self):
        symbols = []

        for market in self.user_input_markets:
            symbols.append(self.markets[market])

        self.week_analyser.set_symbols(symbols)
        self.month_analyser.set_symbols(symbols)

        self.week_analyser.run()
        self.month_analyser.run()
