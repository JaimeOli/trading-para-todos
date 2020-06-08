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
        price = self.data.Close[-1]
        ma1 = self.ma1
        ma2 = self.ma2
        ma3 = self.ma3 

        #Funcion para evaluar si un precio se encuentra del rango permitido con base en la poscion de apertura
        def isinrange(self,price,pos_open):
            if(price > pos_open + self.diff or price < pos_open + self.diff):
                return True
            else:
                return False

        if(not self.position and
           ma1[-1] < ma3[-1] and
           ma2[-1] < ma1[-1] and
           ma2[-1] < ma3[-1]
           ):
            self.buy()
            print('Compre a:' + str(price))
        
        if(ma2[-1] > ma1[-1]):
            self.position.close()

        if(not self.position and
           ma1[-1] > ma3[-1] and
           ma2[-1] > ma1[-1] and
           ma2[-1] > ma3[-1]
           ):
            self.sell()
            print('Vendi a:' + str(price))
        
        if(ma2[-1] < ma1[-1]):
            self.position.close()