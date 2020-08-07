import pandas as pd
import numpy
import talib
import datetime
from itertools import tee, islice, chain

def Dataframe(serie):
    return pd.DataFrame(serie ,columns=["RSI"])

def Dataframe(data,index):
    return pd.DataFrame(data=data,index=index,columns=["RSI"])

def RSI(close,timeperiod):
    return talib.RSI(close,timeperiod)

def RSIDataframe(close,timeperiod):
    return pd.DataFrame(talib.RSI(close,timeperiod),columns=["RSI"])

def CustomRSIdf(dfclose,timeperiod):
    custom = dfclose['Close'].replace(dfclose['Close'].tolist(),talib.RSI(dfclose['Close'],timeperiod))
    custom = custom.rename('RSI')
    return custom.to_frame()

# Analizar rangos de 40 valores ver cuales tienen “RSI (base 7) >70%”
def RSImorethan70(dfrsi):
    rsimore70 = dfrsi.query("RSI > 70")
    if len(rsimore70.index) > 0:
        return rsimore70
    else:
        return False

def TopRSI70(dfrsi70):
    top70 =  []
    index = []
    cnt = 0
    for previous, item, nxt in previous_and_next(dfrsi70.values.tolist()):
        #print("Prev:{}, Nxt:{}, item:{},type:{}".format(str(previous),str(nxt),str(item),str(type(item))))
        if previous is None:
            if item >= nxt:
                top70.append(item)
                index.append(dfrsi70.index[cnt])
        else:
            if nxt is None:
                if item >= previous:
                    top70.append(item)
                    index.append(dfrsi70.index[cnt])
            else:
                if item >= nxt and item >= previous:
                    top70.append(item)
                    index.append(dfrsi70.index[cnt])
        cnt = cnt + 1
    print(cnt)
    return pd.DataFrame(top70,columns=['RSI'],index=index)

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

def top2rsivalues(dfrsi):
    dfm70 = RSImorethan70(dfrsi)
    return dfm70.nlargest(2,'RSI')

def defineinitialCpoints(top2,data):
    top2 = top2rsivalues(dfrsi)
    if top2.index[0] < top2.index[1]:
        return data
    else:
        return data

def diftime(time1,time2):
    difference = time1-time2
    seconds_in_day = 24 * 60 * 60
    difmin = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    return difmin

def changetendency(ant,up):
    if ant < up:
        return True
    else:
        return False



if __name__ == '__main__':
    from csvreader import BacktestingDataframe 
    AUDUSD = BacktestingDataframe("AUDUSD","12-06-2020").get_dataframe()
    output = talib.CDLEVENINGSTAR(AUDUSD["Open"],AUDUSD["High"],AUDUSD["Low"],AUDUSD["Close"],penetration = 0)
    pd.set_option("display.max_rows",None,"display.max_columns",None)
    rsi = RSIDataframe(AUDUSD["Close"],7)
    top2 = top2rsivalues(rsi)
    #print(rsi)
    print(top2)
    print(AUDUSD.index[1])
    print(AUDUSD.index[5])
    print(diftime(top2.index[0],top2.index[1])[0])
    if diftime(top2.index[0],top2.index[1])[0] > 10:
        print("Es mayor a diez")
    #print(top2.index)