import argparse
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
from core.csvreader import BacktestingDataframe
from strategies.strategy import *

def main():
    #parser = argparse.ArgumentParser(description='Backtesting process to evaluate the efficency of forex strategies.')
    #Simulation.run();
    AUDUSD = BacktestingDataframe("AUDUSD").get_dataframe()
    print(AUDUSD)
    bt = Backtest(AUDUSD,SmaCross,cash=10000, commission=.002)
    bt.run()
    bt.plot()

if __name__ == '__main__':
    main()