import pandas as pd
import api_keys
import symbols
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import json
from datetime import datetime
import s3fs
import requests
import time
import os

api_key = api_keys.api_key
key_index = 0

def get_data(symbol):
    symbol = symbol+".BSE"
    global key_index
    key = api_key[key_index]

    url = f' https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={key}'

    response = requests.get(url)
    data = response.json()

    if not os.path.exists("data"): 
        os.makedirs("data") 

    if 'Time Series (Daily)' in data:
        # Process and store the data (example: write to CSV)
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df.to_csv(f'data//{symbol}_stock_data.csv')

    if (key_index + 1) % 25 == 0:
        key_index = (key_index + 1) % len(key)

    time.sleep(5)


def main():

    ticker_symbols = symbols.onlyTatas

    for symbol in ticker_symbols:
        get_data(symbol)

if __name__ == "__main__":
    main()

