# -*- coding: utf-8 -*-
"""
"""
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like #datareader problem probably fixed in next version of datareader
from pandas_datareader import data as pdr
import datetime

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

#Example1
# download dataframe
#data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
# download Panel
#data2 = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")
#example2
#start = datetime.datetime(2017, 1, 1)
#symbol = 'SPY'
#data = pdr.get_data_yahoo(symbol, start=start, end=end)
#data.to_csv("C:\\Users\\Rosario\\Documents\\NeuralNetworksMachineLearning\\LSTMReturnPrediction\\data\\YahooSPY.csv")

start_date=datetime.datetime(1990, 1, 9)
end_date=datetime.datetime(2020, 1, 9)
#end_date= datetime.datetime.now()



stock_list = ["^OEX"]  


stock_str = ""
for i in range(len(stock_list)):
    stock_str  = stock_str + stock_list[i] + "."


for stock in range(len(stock_list)):
     df = pdr.get_data_yahoo(stock_list[stock], start=start_date, end=end_date)
     df.drop(['Adj Close'], axis=1, inplace=True)

df.to_csv(stock_str+"csv")
df = pd.read_csv("^OEX.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Date']=df['Date'].dt.strftime('%Y%m%d')
df.to_csv("OEX.txt", header=None, index=None, sep=' ', mode='a')
df.drop(['Volume'], axis=1, inplace=True)
df.to_csv("OEX2.txt", header=None, index=None, sep=' ', mode='a')


    

