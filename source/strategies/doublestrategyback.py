from backtesting import Strategy
from core.startegiesfunctions import *
import pandas as pd

class DoubletopDoublebottomBacktesting(Strategy):
    def init(self):
        self.rsi7 = self.I(RSI,self.data.Close,7)
        self.counter = 0
        self.C1 = 0
        self.C2 = 0
        self.C3 = 0
        self.C4 = 0
        self.C5 = 0
        self.C6 = 0
        self.C7 = 0
        self.TopRSI70 = TopRSI70(RSImorethan70(CustomRSIdf(self.data.Close.df,7)))
        self.RSI = CustomRSIdf(self.data.Close.df,7)
        self.RSITA = RSI(self.data.Close.df,7)
    def next(self):
        if self.counter == 0:
            print(self.RSI)
        self.counter = self.counter + 1
        #print(self.data.Close.df.index[-1])
        #if self.data.Close.df.index[-1] == :
            #print(dfrsi)
            #print(self.data.index)
            #print(RSImorethan70(dfrsi))
            #print("Funcione son"+ str(self.datalen))
        
        