# -*- coding: utf-8 -*-
"""DarvasBox.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aWkpqLichirjiGZmrs07MXiDofb6FyJU
"""

!pip install nsepython yfinance

!pip install pandas

import yfinance as yf
import pandas as pd
import numpy as np

def calculate_darvas_box(data):
    data['High_max'] = data['High'].rolling(window=260).max()
    data['Low_min'] = data['Low'].rolling(window=260).min()
    data['Volume_SMA_20'] = data['Volume'].rolling(window=20).mean()
    data['SMA_100'] = data['Close'].rolling(window=100).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()

    # Darvas Box conditions
    # Latest High >= Max(260)
    condition1 = data['High'] >= data['High_max'] * 0.8
    # Latest Low >= Min(260)
    condition2 = data['Low'] >= data['Low_min'] * 1.2
    # Close >= SMA(100) and Close >= SMA(200)
    condition3 = (data['Close'] > data['SMA_100']) & (data['Close'] > data['SMA_200'])
    # Latest High < Max(260) and Latest Low > Min(260)
    condition4 = (data['High'] < data['High_max']) & (data['Low'] > data['Low_min'])
    # RSI(14) >= 55
    data['RSI_14'] = 100 - (100 / (1 + data['Close'].diff(1).apply(lambda x: np.exp(x)).rolling(window=14).mean()))
    condition5 = data['RSI_14'] >= 55
    # Volume > SMA(Volume, 20)
    condition6 = data['Volume'] > data['Volume_SMA_20']
    # EPS > 0
    condition7 = data['EPS'] > 0
    # Debt-to-equity ratio < 1
    condition8 = data['Debt_Equity_Ratio'] < 1
    # Market cap < 2000
    condition9 = data['Market_Cap'] < 2000

    # Applying all conditions
    data['Darvas_Box'] = condition1 & condition2 & condition3 & condition4 & condition5 & condition6 & condition7 & condition8 & condition9

    return data[data['Darvas_Box'] == True]


symbol = 'AAPL'
stock_data = yf.download(symbol, start="2022-01-01", end="2024-01-01")
stock_data['EPS'] = 5
stock_data['Debt_Equity_Ratio'] = 0.5
stock_data['Market_Cap'] = 1500

darvas_box_stocks = calculate_darvas_box(stock_data)
print(darvas_box_stocks)

import pandas as pd
darvas_box_stocks_df = pd.DataFrame(darvas_box_stocks)
filename = "DarvasBox_stocks.xlsx"
darvas_box_stocks_df.to_excel(filename, index = False)
print(f"darvas box stocks stored to {filename}")

