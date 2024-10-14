# -*- coding: utf-8 -*-
"""EMADifferenceAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MCWeUjdv81HwaFXxqA1QZbz2PFnTqJPb
"""

import yfinance as yf
import pandas as pd
import numpy as np

# Function to calculate EMA
def calculate_ema(data, period):
    return data['Close'].ewm(span=period, adjust=False).mean()

# Load stock symbols from the CSV file
csv_file_path = '/content/NSE_stocks.csv'  # Update path to your file
stock_data = pd.read_csv(csv_file_path)

# List of stock symbols from the "SYMBOL" column
stock_symbols = stock_data['SYMBOL'].tolist()

# Function to find stocks based on the EMA condition
def find_ema_stocks(stock_symbols):
    qualifying_stocks = []

    for symbol in stock_symbols:
        try:
            # Fetch historical data for the last year to ensure we have enough data
            stock_df = yf.download(symbol + ".NS", period='1y', interval='1d')  # ".NS" for NSE stocks

            if stock_df.empty or len(stock_df) < 21:
                print(f"No sufficient data for {symbol}. Skipping...")
                continue

            # Calculate EMA9 and EMA21
            stock_df['EMA9'] = calculate_ema(stock_df, 9)
            stock_df['EMA21'] = calculate_ema(stock_df, 21)

            # Calculate the absolute difference between EMA21 and EMA9
            stock_df['EMA_diff'] = abs(stock_df['EMA21'] - stock_df['EMA9'])

            # Check today's and 10 days ago's EMA differences
            today_ema_diff = stock_df['EMA_diff'].iloc[-1]  # Today's EMA difference
            ten_days_ago_ema_diff = stock_df['EMA_diff'].iloc[-11]  # EMA difference 10 days ago

            # Apply the conditions
            if today_ema_diff < 4 and ten_days_ago_ema_diff > 4:
                qualifying_stocks.append(symbol)

        except Exception as e:
            print(f"Error processing {symbol}: {e}")

    return qualifying_stocks

# Find the stocks that meet the conditions
qualifying_stocks = find_ema_stocks(stock_symbols)

# Output the qualifying stocks
print("Stocks with today's EMA difference < 4 and 10 days ago > 4:")
for stock in qualifying_stocks:
    print(stock)

qualifying_stocks_df = pd.DataFrame(qualifying_stocks)
qualifying_stocks_df.to_csv("Stocks_with_today's_EMAdiff_10days_diff.csv")