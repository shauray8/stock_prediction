import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import mplfinance as mpf
import matplotlib.dates as mdates

style.use('ggplot')

df = pd.read_csv('./data/tsla.csv',parse_dates=True,index_col=0 )

# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# df.dropna(inplace=True)

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_ohlc['volume'] = df['Volume'].resample('10D').sum()

print(df_ohlc.tail())

mpf.plot(df_ohlc, type='candle', mav=(10), volume=True)
