from Analyser import Analyser
from controller.analyser.WeekAnalyser import WeekAnalyser

import ccxt

analyser = Analyser()
week_analyser = WeekAnalyser()

week_analyser.run()
