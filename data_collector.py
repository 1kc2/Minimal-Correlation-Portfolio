import pandas_datareader as pdr
import datetime
import pandas as pd
from stocks import tickers

# enter the dates for which to collect data
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2020, 7, 31)

start_date_str = str(start.date())
end_date_str = str(end.date())

stocks = tickers

for ticker in stocks:
    file_name = 'data/' + ticker + '_' + start_date_str + '_to_' + end_date_str + '.csv'
    print(file_name)
    data = pdr.DataReader(ticker, 'yahoo', start, end)
    print(data.shape)
    data.to_csv(file_name)

for (i, ticker) in enumerate(stocks):
    file_name = 'data/' +  ticker + '_' + start_date_str + '_to_' + end_date_str + '.csv'
    print(file_name)
    data = pd.read_csv(file_name, parse_dates=['Date'], index_col=['Date'])
    print(data.shape)
    data['Name'] = ticker
    data.to_csv(file_name)
    
    if i == 0:
        all_stocks = data
    else:
        all_stocks = all_stocks.append(data)
        
print(all_stocks.shape)
all_stocks_file_name = 'all_stocks_' + start_date_str + '_to_' + end_date_str + '.csv'
all_stocks.to_csv(all_stocks_file_name)