# StockAnalysis_Patterns-Indicators
Performing stocking analysis by calculating stock indicators and identifying patterns using nsepython and yfinance libraries 
We use live and past data of SBIN from nsepython and yfinance libraries
This project consists of multiple notebooks in which we calculated stock indicators and identify patterns, also the minutes data needed for further stock analysis. Most of the codes uses SBIN symbol for a single stock analysis
1) Firstly I calculated macd, macd signal, rsi, rsi signal and plotted them. For RSI and RSI signal i used "ta" library in python
2) Secondly I calculated EMA(equally weighted moving average), here i calculated EMA30,EMA50, EMA100 and EMA200
3) In the 3rd, I calculated the trend, an important element in stock analysis. Here I calculated Uptrend and DownTrend.
4) Then, I calculated Minimum and Maximum Closing Price of a stock
5) At 5th , I calculated Volume of a stock and also Minumum Volume and Maximum Volume
6) AT 6th , I calculated 
    1. EMA-13 for all dates : EMA for 13 days
    2. EMA-34 for all dates : EMA for 34 days
    3. Regular ATR (Average True Range) for all dates ,reference: https://www.investopedia.com/terms/a/atr.asp . Use n=14
    4. Supertrend ATR (Average True Range) for all dates , reference: https://www.investopedia.com/terms/a/atr.asp . Use n=10
    5. Super-trend for all dates, reference : https://www.investopedia.com/supertrend-indicator-7976167 . Formula mentioned on this page :  Use “Multipler” as 10. 
    6. RVGI (Relative Vigor Index) for all dates and it’s corresponding signal line, reference : Formula and details here https://www.investopedia.com/terms/r/relative_vigor_index.asp
7) AT 7th, I Wrote a function to print list of uptrend 
        1. (Start Date, End Date)-pair
        2. Higher Highs 
        3. Higher Lows
    2. Write a function to print list of downtrend 
        1. (Start Date, End Date)-pair
        2. Lower Highs
        3. Lower Lows
    3. Price Uptrend Data List
    4. Price Downtrend Data List
    5. RSI Uptrend Data List
    6. RSI Downtrend Data List
    7. Find Pair of RSI Divergence Dates : 
        1. Positive Divergence : Price making lower Low and RSI making higher High. Price in Downtrend, RSI Uptrend. Price going to rise in future. Bullish
        2. Negative Divergence : Price making Higher High and RSI making Lower Low. Price in Uptrend, RSI Downtrend. Price going to fall in future. Bearish
For the 7th i also plotted valleys and peaks for each task of uptrend, downtrend and also for the Positive Divergence and Negative Divergence.
8) At 8th, I performed two two tasks.
    1. I Found all triplets - (Date, RSI, MACD) - when MACD turns upwards and is below Signal Line, ie, continuously decreasing reading and then one reading increases from the previous reading. Also, plotted them
    2. I Found all triplets - (Date, RSI, MACD) - when MACD turns downwards and is above Signal Line, ie, continuously increasing reading and then one reading decreases from the previous reading. Also, plotted them
9) At 9th, Then I calculated Patterns for a stock. This is a very key element for our Stock anyalysis. Here i identified and calculated popular patterns of a stock.
Bearish Thrusting in prior uptrend
        1. Pre-requisite : Continuous uptrend (min two Close Price in increasing order) till Date D.
        2. Open Price of D+1 is < Close Price of D, AND
        3. Close Price of D+1 < Open Price of D
        4. And [Open_Price_D + 0.5 * ABS_DIFF(Close_Price_D - Open_Price_D)] < Open_Price_D1
    5. Find all dates with desired patterns : Bullish Piercing in prior downtrend
        1. Pre-requisite : Continuous downtrend (min two Close Price in decreasing order) till Date D.
        2. Open Price of D+1 is < Close Price of D, AND
        3. Close Price of D+1 < Open Price of D
        4. And [Close_Price_D + 0.5 * ABS_DIFF(Close_Price_D - Open_Price_D)] < Close_Price_D1
    6. Find all dates with desired patterns : Bearish Piercing in prior uptrend
        1. Pre-requisite : Continuous uptrend (min two Close Price in increasing order) till Date D.
        2. Open Price of D+1 is > Close Price of D, AND
        3. Close Price of D+1 > Open Price of D
        4. And [Open_Price_D + 0.5 * ABS_DIFF(Close_Price_D - Open_Price_D)] > Open_Price_D1
    7. Find all dates with desired patterns : Tweezer Bottom in prior downtrend
        1. Pre-requisite : Continuous downtrend (min two Close Price in decreasing order) till Date D.
        2. Low Price of D+1 = Low Price of D +/- (0.1)
    8. Find all dates with desired patterns : Tweezer Top in prior uptrend
        1. Pre-requisite : Continuous uptrend (min two Close Price in increasing order) till Date D.
        2. High Price of D+1 = High Price of D +/- (0.1)
    9. Find all dates with gap-up openings : Open Price of D+1 > High Price of D 
    10. Find all dates with gap-down opening : Open Price of D+1 < Low Price of D 
    11. Find all possible triplets (stock name, date, Pattern) with desired patterns and print in an excel
PS: To calculate pattern on date D and D+1 (as there are two candles to be compared), we define Prior Uptrend as : Stock should be in uptrend from date D-2 to date D (that is for 3 continuous days). Similarly, prior downtrend means it should be in continuous downtrend from D-2 to D
11) Then, I wrote a code for few patterns and plotted them for further analysis. Below are the patterns i coded for p
    1. Plot 1 : Stock Price vs Time, over last 90 days 
    2. Plot 2 : RSI vs Time, over last 90 days
    3. Plot 3 : MACD vs Time, over last 90 days
    4. Plot 4 : ATR vs Time, over last 90 days
12) Then I coded a function - which when called, downloads the stock data for the “Specific Date’ input and appends to the end of the excel. Idea is to call this function everyday once such that the Price_stockName.xlsx is kept upto date and we don’t download entire 5 year data everyday as it’s a waste of resource bandwidth
13) I calculated market cap for all the 1967 stocks present in NSE using yfinance library. Using market cap we can determine the growth and if it's large or medium or small cap for a company 


