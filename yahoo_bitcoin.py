"""

"""


import datetime as dt
import pandas as pd
import pandas_datareader.data as web

symbol= 'BTC-USD'

start= dt.datetime(2019,3,1)
end = dt.datetime(2019,4,1)
df = web.DataReader(symbol, 'yahoo', start, end)
df.to_csv('yahoo_bitcoin.csv')
print (df)
df = pd.read_csv('yahoo_bitcoin.csv',parse_dates=True,index_col=0 )
df = df.round(4)
df.to_csv('yahoo_bitcoin.csv')

