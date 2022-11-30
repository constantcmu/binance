import streamlit as st
import yfinance as yf
import pandas as pd


st.title("List Finance Dashboard")
tickers = ("TSLA",'AAPL','BTC-USD','ETH-USD',"BNB-USD","ADA-USD","goog", "amzn", "BAC", "BA")

dropdown = st.multiselect('Pick your assets',
                        tickers)
start = st.date_input('Start',value=pd.to_datetime('2020-01-01'))
end = st.date_input("End",value=pd.to_datetime('today'))


def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumert = cumret.fillna(0)
    return cumert

if len(dropdown)>0:
    # df = yf.download(dropdown,start,end)["Adj Close"]
    df = relativeret(yf.download(dropdown,start,end)["Adj Close"])
    
    st.line_chart(df)




