from controller.DbController import DbController
from models.MonthAnalysis import MonthAnalysis
from datetime import datetime, timedelta
from calendar import monthrange


class MonthAnalyser:

    def __init__(self):
        self.db_controller = DbController()

        self.symbols = []

    def run(self):
        for symbol in self.symbols:
            self.analyse_symbol(symbol)

    def analyse_symbol(self, symbol):
        candles = self.db_controller.get_candles(symbol=symbol, timeframe='1w')

        current_month = None
        current_month_number = None
        current_month_volatility_high = 0
        current_month_volatility_low = 0
        current_month_volume_high = 0
        current_month_volume_low = 0

        months = []

        for candle in candles:
            candle_year = candle.time_readable.isocalendar()[0]
            candle_month_number = candle.time_readable.month

            if current_month_number != candle_month_number:
                if current_month is not None:
                    months.append(current_month)

                current_month_number = candle_month_number

                current_month_volatility_high = candle.volatility
                current_month_volatility_low = candle.volatility
                current_month_volume_high = candle.volume
                current_month_volume_low = candle.volume

                month_start = candle.time_readable
                month_end = month_start + timedelta(days=monthrange(candle_year, candle_month_number)[1])

                current_month = MonthAnalysis(
                    exchange='ftx',
                    symbol=candle.symbol,
                    start_date=month_start,
                    end_date=month_end,
                    open=candle.open,
                    monthly_high=candle.high,
                    monthly_low=candle.low,
                    volume=candle.volume,
                )

            else:
                if candle.high > current_month.monthly_high:
                    current_month.monthly_high = candle.high
                if candle.low < current_month.monthly_low:
                    current_month.monthly_low = candle.low
                if candle.volatility > current_month_volatility_high:
                    current_month_volatility_high = candle.volatility
                if candle.volatility < current_month_volatility_low:
                    current_month_volatility_low = candle.volatility
                if candle.volume > current_month_volume_high:
                    current_month_volume_high = candle.volume
                if candle.volume < current_month_volume_low:
                    current_month_volume_low = candle.volume

                current_month.close = candle.close
                current_month.volume += candle.volume

        self.db_controller.add_entries(months)

    def set_symbols(self, symbols):
        self.symbols = [*symbols]
