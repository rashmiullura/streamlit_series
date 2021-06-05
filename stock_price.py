import yfinance as yf
import streamlit as st
import pandas as pd
from yfinance import ticker

#Simple Stock Price App -> header 
#Shown are the stock closing price and volume of Google! -> normal text
# ** .. ** ->bold

st.write("""
# Simple Stock Price App  

Shown are the stock **closing price** and **volume** of Google! 

""")

#define the ticker symbol of google
tickerSymbol = 'GOOGL'

#get data on the ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker 
tickerDf = tickerData.history(period="Id", start="2010-5-31", end="2021-5-31")

#Open High Low Close Volume Dividends Stock Split --> columns 
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)