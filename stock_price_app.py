import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App 

Shown are the stock closing price and volume of Google!

""")

# define the tiker sybol
symbolTicker = 'GOOGL'
# get data on this ticker
dataTicker = yf.Ticker(symbolTicker)
# get the history of the prices for the ticker above
dfTicker = dataTicker.history(period='1d', start='2010-5-3', end='2022-1-5')
# Open High Low Close Volume Dividends Stock Splits
st.line_chart(dfTicker.Close)
st.line_chart(dfTicker.Volume)
