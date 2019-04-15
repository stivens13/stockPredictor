import matplotlib.pyplot as plt
import requests
import pandas as pd
from pandas import DataFrame


r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2019-03-01&end=2019-04-01').json()
print(r)
#sending jason file into the dat frame
df = pd.DataFrame(r, columns=['bpi'])
#df.to_csv('coindesk.csv')
print (df.info())
# drop the null values
df.dropna(inplace=True)

#split a cloumn to two column

#since "bpi" is one columns with values and key dictionary type

# sending values of the bpi as price
Price = df['bpi'].values
print (Price)

# sending key (Dates) of the bpi as Date
Date= df['bpi'].keys()
print (Date)

# making a new data frame with columns labels
newDf = pd.DataFrame(columns=['Date','Close'])
newDf['Date']= Date # fill the column with Date
newDf['Close']= Price# fill the column with Prices

newDf.to_csv('coindesk.csv')
