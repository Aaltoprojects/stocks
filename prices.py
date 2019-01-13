import datetime as dt
import time
import matplotlib.pyplot as plt
import matplotlib.axes as pltx
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

def correlation(df):

	change = abs(df['Adj Close'] - df['Open'])
	vol = df['Volume']

	return vol.corr(change)

names = []
ids = []

#save names and ids to variables
for i in range(3427):
	names.append(str(sheet.cell_value(i+1, 1)))
	ids.append(str(sheet.cell_value(i+1, 0)))

#original correlations' request script
'''
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

	return correlations

'''

file = open('dataframes.obj', 'rb')
datadic = pickle.load(file)
file.close()

#print(datadic.keys())
#number of keys in dictionary
#print(len(datadic.keys()))
#print(datadic['ZNGA'])

correlations = []
topcompanies = {}

for i in datadic:

	if str(correlation(datadic[i])) == 'nan':
		
		print('poistettu')

	else:

		correlations.append(correlation(datadic[i]))

		if correlation(datadic[i]) >= 0.80:

			topcompanies[str(i)] = correlation(datadic[i])


print(len(correlations))
correlations.sort()

print(correlations[2994:3019])

print('top:\n')
print(topcompanies)


'''
plt.plot(datadic['AMTX']['Adj Close'])
plt.plot(datadic['AMTX']['Volume'])
plt.show()
'''
vol = datadic['AMTX']['Volume']
change = abs(datadic['AMTX']['Adj Close'] - datadic['AMTX']['Open'])
print(vol.corr(change))

plt.figure()
plt.scatter(vol, change)
ax = plt.gca()
ax.set_xlim([0, 100000])
ax.set_ylim([-0.05, 0.15])
plt.show()

#creates dictionary of ids and dataframes
#dict = {}

'''
tässä kirjoitettiin .obj tiedostoon dataframet ja avaimiksi osakelyhenteet

for i in range(3427):
	if names[i+1] != names[i]:
		try:
			time.sleep(3)
			df = web.DataReader(ids[i+1], 'yahoo', start, end)
			dict[ids[i+1]] = df
			print(names[i+1] + '\n')
		except:
			print('No price data\n')
	else: print('Bad stock\n')

#write dataframes to .obj file
file = open("NIMI.TYYPPI", 'wb')
pickle.dump(dict, file)
file.close()
'''

#read dataframes from .obj file
#file2 = open('NIMI.TYYPPI', 'rb')
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