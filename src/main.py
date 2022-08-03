from Analyser import Analyser
from controller.analyser.WeekAnalyser import WeekAnalyser
from controller.analyser.MonthAnalyser import MonthAnalyser


analyser = Analyser()
week_analyser = WeekAnalyser()
month_analyser = MonthAnalyser()

analyser.run()
week_analyser.run()
month_analyser.run()


