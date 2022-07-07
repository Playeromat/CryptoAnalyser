from controller.DbController import DbController


class WeekAnalyser:
    def run(self):
        db_controller = DbController()
        candles = db_controller.get_candles()

        for candle in candles:
            print(candle.symbol)
