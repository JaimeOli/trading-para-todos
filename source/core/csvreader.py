import pandas as pd
from datetime import date, timedelta
from pathlib import Path

yesterday = date.today() - timedelta(days=1)

def importcsvdata(divisa,date = yesterday,sep = ',',index = 0):
    csvstring = convert_date_to_csvstring(divisa,date)
    pathfile = add_default_data_path(csvstring)
    return readcsv(pathfile,sep,index)

def convert_date_to_csvstring(divisa,date):
    return date.strftime("{div}-%Y_%m_%d-%Y_%m_%d.csv").format(div = divisa)

def add_default_data_path(csvstring):
    return "{home}/trading/trading-para-todos/data/{csv}".format(home = str(Path.home()), csv = csvstring)

def readcsv(filename,sep,index):
    return pd.read_csv(filename, sep= sep, index_col=index)

if __name__ == '__main__':
    print(importcsvdata("AUDUSD"))