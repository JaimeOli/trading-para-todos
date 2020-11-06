from backtesting import Strategy
from core.startegiesfunctions import *

class DoubletopDoublebottom(Strategy):
    def init(self):
        self.rsi7 = self.I(RSI,self.data.Close,7)
        self.Closedf = self.data.Close.df
        self.Highdf = self.data.High.df
        self.Opendf = self.data.Open.df
        self.rsi7df = CustomRSIdf(self.Closedf,7)
        self.C1 = 0
        self.H1 = 0
        self.C2 = 0
        self.H2 = 0
        self.C3 = 0
        self.C4 = 0
        self.C5 = 0
        self.C6 = 0
        self.C6index = None
        self.C6reach = False
        self.C7 = 0
        self.cnt = 0
        self.rsiminimun = 65
        self.analyserange = 60
        self.validrsi = False
        self.startrsi = None
        self.allCvalidated = False
        self.candlesmindif = 10
    def next(self):
        price = self.data.Close[-2]
        currentprice = self.data.Close[-1]
        currentindex = self.rsi7.df.index[-1]
        nextindex = self.rsi7.df.index[-2]
        #Se verifica que haya un rsi reciente mayor a rsiminimun
        if self.rsi7[-1] >= self.rsiminimun and not self.validrsi:
            self.validrsi = True
            self.startrsi = currentindex
            print("El rsi actual")
            print(self.startrsi)
        #Se ejecuta el codigo a partir del primer rsi mayor a rsiminimun
        if self.validrsi == True and self.allCvalidated == False:
            if self.cnt == self.analyserange:
                #Se verifica que la longitud de los rsi mayores a 67 sea mayor a dos
                fortyvalues = self.rsi7.df.loc[self.startrsi:currentindex]
                print('Valores mayores a 65')
                print(len(RSImorethan(fortyvalues,self.rsiminimun).index))
                if len(RSImorethan(fortyvalues,self.rsiminimun).index) > 2:
                    fortyvalues = changersicolumnname(fortyvalues)
                    top2rsi = top2rsi70values(RSImorethan(fortyvalues,self.rsiminimun))
                    #Se ordena los valores con respecto a la fecha
                    top2rsi = top2rsi.sort_index(axis = 0)
                    #Se verifica que los valores esten separados por 10 mins
                    print("Top 2")
                    print(top2rsi)
                    if diftime(top2rsi.index[1],top2rsi.index[0])[0] >= self.candlesmindif:
                        #print("Valores mayores de 67 y 10 min de diferencia")
                        #print(top2rsi)
                        hrsi = definehighestrsi(top2rsi)
                        if hrsi == top2rsi.index[0]:
                            self.C1 = self.data.Close.df.loc[top2rsi.index[0]]
                            self.H1 = self.data.High.df.loc[top2rsi.index[0]]
                            self.C2 = self.data.Close.df.loc[top2rsi.index[1]]
                            self.H2 = self.data.High.df.loc[top2rsi.index[1]]
                            #Se crea nuevo rango a partir del cual saldran los otros C
                            currentplusrange = addminutes(currentindex,50)
                            if currentindex.day == currentplusrange.day:
                                ninetyvalues =  self.rsi7df.loc[self.startrsi:currentplusrange]
                                self.C3 = self.Closedf.loc[smallestvalue(ninetyvalues).index[0]]
                                smalestrsi2 = smallestvalue(ninetyvalues.loc[top2rsi.index[1]:currentplusrange])
                                posibleC4 = self.Closedf.loc[smalestrsi2.index[0]].values[0]
                                #Se comprueba que C4 este en el intervalo
                                if (posibleC4 >= 2*self.C3-self.C2).bool() and (posibleC4 <= -3.67*self.C3+4.67*self.C2).bool():
                                    if (self.Closedf.loc[currentplusrange] > posibleC4).bool():
                                        self.C4 = posibleC4
                                    else:
                                        self.C4 = self.Closedf.loc[str(currentplusrange)]
                                    highestrsi2 = highestvalue(ninetyvalues.loc[smalestrsi2.index[0]:currentplusrange])
                                    posibleC5 = self.Closedf.loc[highestrsi2.index[0]].values[0]
                                    openC5 = self.Opendf.loc[highestrsi2.index[0]].values[0]
                                    print("C4")
                                    print(self.C4)
                                    print("C5 candidato")
                                    print(posibleC5)
                                    if (posibleC5 >= 0.114*self.C4+0.886*self.C2).bool() and (posibleC5 <= 0.5*self.C4+0.5*self.C2).bool() and openC5 < posibleC5:
                                        if (self.Closedf.loc[currentplusrange] < posibleC5).bool():
                                            self.C5 = posibleC5
                                        else:
                                            self.C5 = self.Closedf.loc[currentplusrange]
                                        print("C5")
                                        print(self.C5)
                                        smalestrsi3 = smallestvalue(ninetyvalues.loc[highestrsi2.index[0]:currentplusrange])
                                        posibleC6 = self.Closedf.loc[smalestrsi3.index[0]].values[0]
                                        if (self.C5 < posibleC6).bool():
                                            self.C6 = posibleC6
                                            print("C6")
                                            print(self.C6)
                                            self.C6index = smalestrsi3.index[0]
                                            self.C7 = self.C4 + 0.236*(self.C2-self.C4)
                                            self.allCvalidated = True
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            self.C1 = self.data.Close.df.loc[top2rsi.index[1]]
                            self.H1 = self.data.High.df.loc[top2rsi.index[1]]
                            self.C2 = self.data.Close.df.loc[top2rsi.index[0]]
                            self.H2 = self.data.High.df.loc[top2rsi.index[0]]
                            #Se crea nuevo rango a partir del cual saldran los otros C
                            currentplusrange = addminutes(currentindex,50)
                            if currentindex.day == currentplusrange.day:
                                ninetyvalues =  self.rsi7df.loc[self.startrsi:currentplusrange]
                                self.C3 = self.Closedf.loc[smallestvalue(ninetyvalues).index[0]]
                                smalestrsi2 = smallestvalue(ninetyvalues.loc[top2rsi.index[1]:currentplusrange])
                                posibleC4 = self.Closedf.loc[smalestrsi2.index[0]].values[0]
                                #Se comprueba que C4 este en el intervalo
                                if (posibleC4 >= 2*self.C3-self.C2).bool() and (posibleC4 <= -3.67*self.C3+4.67*self.C2).bool():
                                    if (self.Closedf.loc[currentplusrange] > posibleC4).bool():
                                        self.C4 = posibleC4
                                    else:
                                        self.C4 = self.Closedf.loc[str(currentplusrange)]
                                    highestrsi2 = highestvalue(ninetyvalues.loc[smalestrsi2.index[0]:currentplusrange])
                                    posibleC5 = self.Closedf.loc[highestrsi2.index[0]].values[0]
                                    openC5 = self.Opendf.loc[highestrsi2.index[0]].values[0]
                                    print("C4")
                                    print(self.C4)
                                    if (posibleC5 >= 0.114*self.C4+0.886*self.C2).bool() and (posibleC5 <= 0.618*self.C4+0.382*self.C2).bool() and openC5 < posibleC5:
                                        if (self.Closedf.loc[currentplusrange] < posibleC5).bool():
                                            self.C5 = posibleC5
                                        else:
                                            self.C5 = self.Closedf.loc[currentplusrange]
                                        print("C5")
                                        print(self.C5)
                                        smalestrsi3 = smallestvalue(ninetyvalues.loc[highestrsi2.index[0]:currentplusrange])
                                        posibleC6 = self.Closedf.loc[smalestrsi3.index[0]].values[0]
                                        if (self.C5 < posibleC6).bool():
                                            self.C6 = posibleC6
                                            print("C6")
                                            print(self.C6)
                                            self.C6index = smalestrsi3.index[0]
                                            self.C7 = self.C4 + 0.236*(self.C2-self.C4)
                                            self.allCvalidated = True
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                    self.validrsi = False
                    self.cnt = 0
                else:
                    self.validrsi = False
                    self.cnt = 0
            self.cnt += 1
        #Comienza la ejecucion de la venta
        if self.allCvalidated == True:
            if self.C6index == nextindex:
                self.C6reach = True
                self.sell()
                print(str(date) + ' Vendí a:' + str(price))
            if self.C6reach == True:
                if currentprice >= self.C7:
                    self.position.close()
                    self.C6reach = False
                    self.allCvalidated = False