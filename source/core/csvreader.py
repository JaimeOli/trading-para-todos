import pandas as pd
from datetime import date, timedelta, datetime
from pathlib import Path

class BacktestingDataframe:
    #Se usa yesterady como valor por defecto si no se da una fecha
    yesterday = date.today() - timedelta(days=1)

    def __init__(self,divisa,paramdate = yesterday,sep = ',',csv_filename = None):
        if csv_filename is None:
            if isinstance(paramdate,date):
                self.dataframe = self.importcsvdata(divisa,paramdate,sep)
            else:
                try:
                    paramdate = datetime.strptime(paramdate,"%d-%m-%Y")
                    self.dataframe = self.importcsvdata(divisa,paramdate,sep)
                except NameError:
                    print(NameError)
        else:
            pass
    
    def get_dataframe(self):
        return self.dataframe

    def importcsvdata(self,divisa,date,sep):
        def convert_date_to_csvstring(divisa,date):
            return date.strftime("{div}-%Y_%m_%d-%Y_%m_%d.csv").format(div = divisa)

        def add_default_data_path(csvstring):
            return "{home}/trading/trading-para-todos/data/{csv}".format(home = str(Path.home()), csv = csvstring)

        def readcsv(filename,sep):
            return pd.read_csv(filename, sep= sep, index_col=['time'],parse_dates=True)

        csvstring = convert_date_to_csvstring(divisa,date)
        pathfile = add_default_data_path(csvstring)
        dataframe = readcsv(pathfile,sep)
        dataframe.rename(columns={'open':'Open','close':'Close','high':'High','low':'Low'},inplace=True)
        print(dataframe.columns)
        self.dataframe = dataframe
        return dataframe

if __name__ == '__main__':
    data = BacktestingDataframe('AUDUSD').get_dataframe()
    print(data[['Open']][:1])
    print(data)