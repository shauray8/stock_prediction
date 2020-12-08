import datetime as dt 
import pandas as pd 
import pandas_datareader.data as web

start = dt.datetime(2015,1,1)
end = dt.datetime(2020,11,30)

df = web.DataReader('TSLA', 'yahoo', start, end)

# print(df.head())
df.to_csv('tsla.csv')