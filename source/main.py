import argparse
from backtesting import Strategy
from core.simulation import run_array_simulation
from strategies.strategy import ThreeSma
from strategies.doublestrategy import DoubletopDoublebottom
from strategies.doublestrategyback import DoubletopDoublebottomBacktesting

def main():
    #parser = argparse.ArgumentParser(description='Backtesting process to evaluate the efficency of forex strategies.')
    #Simulation.run();
    #AUDUSD = BacktestingDataframe("AUDUSD","27-05-2020").get_dataframe()
    parser = argparse.ArgumentParser()
    #El primer parametro es la estrategia con la cual se van a realizar las simulaciones
    parser.add_argument("strategy",
    help="the name of the strategy wich you want to use",
    type=str
    )
    #El segundo parametro que se pide es una inversion con la cual se va realizar la simulacion
    parser.add_argument("investment", 
    help="it is the intial investment at the moment of the simulation",
    nargs='?',
    type=int, 
    default=10000)
    #El tercer parametro es una comision que cobra al momento de realizar una transaccion
    parser.add_argument("comission", 
    help="the percent that is collected each time a transaction is completed", 
    type=float,
    nargs='?',
    default=0.0002)

    args = parser.parse_args()
    if args:
        currencies = ["XAUUSD","AUDUSD","NZDUSD","EURUSD","USDJPY","EURJPY","GBPUSD"]
        dates = ["06-08-2020"]
        try:
            strategy = convert_to_strategy_type(args.strategy)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

        run_array_simulation(strategy,args.investment,args.comission,currencies,dates)

def convert_to_strategy_type(string):
    if string == "ThreeSma":
        return ThreeSma
    if string == "DoubleTopBack":
        return DoubletopDoublebottomBacktesting
    if string == "DoubleTop":
        return DoubletopDoublebottom
    else:
        raise Exception ("Not strategy match found")

if __name__ == '__main__':
    import core.getdataviaduka as duka
    #duka.getdukadata()
    main()
