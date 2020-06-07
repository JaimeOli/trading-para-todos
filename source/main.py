import argparse
from backtesting import Backtest, Strategy
from core.csvreader import BacktestingDataframe
from strategies.strategy import *

def main():
    #parser = argparse.ArgumentParser(description='Backtesting process to evaluate the efficency of forex strategies.')
    #Simulation.run();
    #AUDUSD = BacktestingDataframe("AUDUSD","27-05-2020").get_dataframe()
    parser = argparse.ArgumentParser()
    parser.add_argument("investment", 
    help="it is the intial investment at the moment of the simulation",
    type=int)
    parser.add_argument("comission", 
    help="the percent that is ",
    type=float)
    parser.parse_args()
    args = parser.parse_args()
    if args:
        currencies = ["XAUUSD","AUDUSD","NZDUSD","EURUSD","USDJPY","EURJPY","GBPUSD"]
        dates = ["05-06-2020","05-06-2020","05-06-2020","05-06-2020","05-06-2020","05-06-2020","05-06-2020"]
        run_array_simulation(SmaCross,args.investment,args.comission,currencies,dates)

def run_array_simulation(strategy,cash,commission,currencies,dates = None):
    if dates is None:
        for currency in currencies:
            df = BacktestingDataframe(currency).get_dataframe()
            bt = Backtest(df,strategy,cash=cash, commission=commission)
            print(bt.run())
            bt.plot(filename="{currency}.html".format(currency = currency),open_browser=False)
    else:
        for date in dates:
            for currency in currencies:
                df = BacktestingDataframe(currency,paramdate = date).get_dataframe()
                bt = Backtest(df,strategy,cash=cash, commission=commission)
                print(bt.run())
                bt.plot(filename="{currency}.html".format(currency = currency),open_browser=False)

if __name__ == '__main__':
    main()