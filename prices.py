import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#select the time period of the stock data
start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

#save the price data of Tesla from yahoo finance api to a dataframe variable
df = web.DataReader('TSLA', 'yahoo', start, end)

#create an excel file from the data
df.to_excel('tsla.xlsx')

#read this excel file to a dataframe
df = pd.read_excel('tsla.xlsx', parse_dates = True, index_col = 0)

#print(df.head())



df['Adj Close'].plot()
plt.show()