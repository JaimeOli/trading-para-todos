import argparse
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
from core.csvreader import BacktestingDataframe
from strategies.strategy import *

def main():
    #parser = argparse.ArgumentParser(description='Backtesting process to evaluate the efficency of forex strategies.')
    #Simulation.run();
    #AUDUSD = BacktestingDataframe("AUDUSD","27-05-2020").get_dataframe()
    currencies = ["XAUUSD","AUDUSD","NZDUSD","EURUSD","USDJPY","EURJPY","GBPUSD"]
    run_array_simulation(SmaCross,10000,.002,currencies)

def run_array_simulation(strategy,cash,commission,currencies,dates = None):
    if dates is None:
        for currency in currencies:
            df = BacktestingDataframe(currency).get_dataframe()
            bt = Backtest(df,strategy,cash=cash, commission=commission)
            print(bt.run())
            bt.plot(filename="{currency}.html".format(currency = currency),open_browser=False)
    else:
        pass

if __name__ == '__main__':
    main()