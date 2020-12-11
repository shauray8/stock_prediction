import datetime as dt
import pickle
import os
import pandas as pd 
import pandas_datareader.data as web

infile = open('sp500tickers.pickle','rb')

tickers =pickle.load(infile)
tickers[66] = 'BRK'
tickers[79] = 'BR'
def get_data_from_yahoo():
	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')

	start = dt.datetime(2015,1,1)
	end = dt.datetime(2020,11,30)
	i = 0
	for ticker in tickers:
		i += 1
		if not os.path.exists(f'stock_dfs/{ticker}.csv'):
			df = web.DataReader(ticker, 'yahoo', start, end)
			df.to_csv(f'stock_dfs/{ticker}.csv')
			print(f"parsing stock number: {i} stock ticker: {ticker}")
		else:
			print(f"Already have {ticker}")

get_data_from_yahoo()
# print(tickers[79])
