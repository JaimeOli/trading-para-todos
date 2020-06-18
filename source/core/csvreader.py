import pandas as pd
from datetime import date, timedelta, datetime
import os

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
            self.dataframe = pd.read_csv(csv_filename, sep= sep, index_col=['time'],parse_dates=True)
    
    def get_dataframe(self):
        return self.dataframe
        
    def importcsvdata(self,divisa,date,sep):
        def convert_date_to_csvstring(divisa,date):
            return date.strftime("{div}-%Y_%m_%d-%Y_%m_%d.csv").format(div = divisa)

        def add_default_data_path(csvstring):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            return "{home}/../../data/{csv}".format(home = dir_path, csv = csvstring)

        def readcsv(filename,sep):
            return pd.read_csv(filename, sep= sep, index_col=['time'],parse_dates=True)
        
        def renamedukacsvcolumns(df):
            return df.rename(columns={'open':'Open','close':'Close','high':'High','low':'Low'},inplace=True)

        csvstring = convert_date_to_csvstring(divisa,date)
        pathfile = add_default_data_path(csvstring)
        dataframe = readcsv(pathfile,sep)
        renamedukacsvcolumns(dataframe)
        return dataframe

if __name__ == '__main__':
    data = BacktestingDataframe('AUDUSD').get_dataframe()
    print(data.describe())
    print(data.dtypes)
    print(data['Open'])
    print(data[['Open']][:1])
    print(data)