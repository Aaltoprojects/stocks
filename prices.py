import datetime as dt
import time
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import scipy as sp
import xlrd
import xlsxwriter
import pickle

style.use('ggplot')

#select the time period of the stock data
start = dt.datetime(2018,1,1)
end = dt.datetime(2018,12,31)

filename = 'companylist.xlsx'
book = xlrd.open_workbook(filename)
sheet = book.sheet_by_index(0)

def correlation(name):
	df = web.DataReader(name, 'yahoo', start, end)
	change = abs(df['Adj Close'] - df['Open'])
	vol = df['Volume']
	return vol.corr(change)

names = []
ids = []

for i in range(3427):
	names.append(str(sheet.cell_value(i+1, 1)))
	ids.append(str(sheet.cell_value(i+1, 0)))

def volumechangecorr(numofcos):

	correlations = []

	#max index 3428
	for i in range(numofcos):
		if names[i+1] != names[i]:
			try:
				correlations.append(correlation(ids[i+1]))
				print(correlation(ids[i+1]))
				print(names[i+1] + '\n')
			except KeyError:
				print('No price data\n')
		else: print('Bad stock\n')
	return


#creates dictionary of ids and dataframes
dict = {}

for i in range(5):
	if names[i+1] != names[i]:
		try:	
			df = web.DataReader(ids[i+1], 'yahoo', start, end)
			dict[ids[i+1]] = df
			print(names[i+1] + '\n')
		except KeyError:
			print('No price data\n')
	else: print('Bad stock\n')

#write dataframes to .obj file
file = open('dataframes.obj', 'wb')
pickle.dump(dict, file)
file.close()

#read dataframes from .obj file
#file2 = open('dataframes.obj', 'rb')
#testi = pickle.load(file2)
#file2.close()


#correlations.sort()
#plt.plot(correlations)
#plt.show()



#create an excel file from the data
#df.to_excel('AAPL.xlsx')

#read this excel file to a dataframe
#df = pd.read_excel('AAPL.xlsx', parse_dates = True, index_col = 0)

#print(df.head())

# tutorial part 3 next:
# https://www.youtube.com/watch?v=QAkOnV1-lIg

#df['Adj Close'].plot()
#plt.show()

#df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
#df.dropna(inplace=True)

#df['Adj Close'].plot()
#df['10ma'].plot()
#plt.show()