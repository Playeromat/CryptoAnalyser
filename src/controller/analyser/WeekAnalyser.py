from controller.DbController import DbController
from models.WeekAnalysis import WeekAnalysis
from datetime import datetime, timedelta


class WeekAnalyser:

    def __init__(self):
        self.db_controller = DbController()
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def run(self):
        candles = self.db_controller.get_candles(symbol='BTC/USD:USD', timeframe='1d')

        current_week = None
        current_week_number = None
        current_week_volatility_high = 0
        current_week_volatility_low = 0
        current_week_volume_high = 0
        current_week_volume_low = 0

        for candle in candles:
            candle_week_number = candle.time_readable.isocalendar()[1]
            candle_weekday_number = candle.time_readable.isocalendar()[2]

            if current_week_number != candle_week_number:
                if current_week is not None:
                    self.db_controller.add_entry(current_week)

                current_week_number = candle_week_number

                current_week_volatility_high = candle.volatility
                current_week_volatility_low = candle.volatility
                current_week_volume_high = candle.volume
                current_week_volume_low = candle.volume

                week_start = candle.time_readable
                week_end = week_start + timedelta(days=7) - timedelta(seconds=1)

                current_week = WeekAnalysis(
                    exchange='ftx',
                    symbol=candle.symbol,
                    start_date=week_start,
                    end_date=week_end,
                    open=candle.open,
                    weekly_high=candle.high,
                    weekly_low=candle.low,
                    weekday_high=self.weekdays[candle_weekday_number - 1],
                    weekday_low=self.weekdays[candle_weekday_number - 1],
                    weekday_volatility_high=self.weekdays[candle_weekday_number - 1],
                    weekday_volatility_low=self.weekdays[candle_weekday_number - 1],
                    weekday_volume_high=self.weekdays[candle_weekday_number - 1],
                    weekday_volume_low=self.weekdays[candle_weekday_number - 1],
                    volume=candle.volume,
                )

            else:
                if candle.high > current_week.weekly_high:
                    current_week.weekly_high = candle.high
                    current_week.weekday_high = self.weekdays[candle_weekday_number - 1]
                if candle.low < current_week.weekly_low:
                    current_week.weekly_low = candle.low
                    current_week.weekday_low = self.weekdays[candle_weekday_number - 1]
                if candle.volatility > current_week_volatility_high:
                    current_week_volatility_high = candle.volatility
                    current_week.weekday_volatility_high = self.weekdays[candle_weekday_number - 1]
                if candle.volatility < current_week_volatility_low:
                    current_week_volatility_low = candle.volatility
                    current_week.weekday_volatility_low = self.weekdays[candle_weekday_number - 1]
                if candle.volume > current_week_volume_high:
                    current_week_volume_high = candle.volume
                    current_week.weekday_volume_high = self.weekdays[candle_weekday_number - 1]
                if candle.volume < current_week_volume_low:
                    current_week_volume_low = candle.volume
                    current_week.weekday_volume_low = self.weekdays[candle_weekday_number - 1]

                current_week.close = candle.close
                current_week.volume += candle.volume

        self.db_controller.commit()
