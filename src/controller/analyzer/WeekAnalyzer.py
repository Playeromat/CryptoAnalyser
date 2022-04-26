from controller.DbController import DbController


class WeekAnalyzer:
    def run(self):
        db_controller = DbController()
        ohlcvs = db_controller.get_ohlcvs()

        for ohlcv in ohlcvs:
            print(ohlcv.symbol)
