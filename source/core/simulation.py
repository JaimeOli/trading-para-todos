from core.csvreader import BacktestingDataframe
from backtesting import Backtest, Strategy

def run_array_simulation(strategy,cash,commission,currencies,dates = None):
    if dates is None:
        for currency in currencies:
            print(currency)
            df = BacktestingDataframe(currency).get_dataframe()
            bt = Backtest(df,strategy,cash=cash, commission=commission)
            print(bt.run())
            bt.plot(filename="{currency}.html".format(currency = currency),open_browser=False)
    else:
        for date in dates:
            for currency in currencies:
                print(currency)
                df = BacktestingDataframe(currency,paramdate = date).get_dataframe()
                bt = Backtest(df,strategy,cash=cash, commission=commission)
                print(bt.run())
                bt.plot(filename="{currency}.html".format(currency = currency),open_browser=False)
