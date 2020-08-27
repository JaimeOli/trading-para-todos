from backtesting import Backtest
from backtesting.lib import crossover, SignalStrategy, TrailingStrategy
from backtesting.test import SMA

class ThreeSma(SignalStrategy,TrailingStrategy):
    def init(self):
        Close = self.data.Close
        self.ma1 = self.I(SMA, Close, 10)
        self.ma2 = self.I(SMA, Close, 20)
        self.ma3 = self.I(SMA, Close, 30)
        self.diff = 0.0012

    def next(self):
        price = self.data.Close[-2]
        date = self.data.index[-2]
        ma1 = self.ma1
        ma2 = self.ma2
        ma3 = self.ma3 
        
        if(not self.position and
           ma1[-1] < ma3[-1] and
           ma2[-1] < ma1[-1] and
           ma2[-1] < ma3[-1]
           ):
            self.buy()
            print(str(date) + ' Compre a:' + str(price))
        
        if(self.position and ma2[-1] > ma1[-1]):
            self.position.close()

        if(not self.position and
           ma1[-1] > ma3[-1] and
           ma2[-1] > ma1[-1] and
           ma2[-1] > ma3[-1]
           ):
            self.sell()
            print(str(date) + ' Vendi a:' + str(price))
        
        if(self.position and ma2[-1] < ma1[-1]):
            self.position.close()