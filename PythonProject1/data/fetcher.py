import yfinance as yf
import pandas as pd

def get_stock_data(tickers):
    rows = []

    for t in tickers:
        stock = yf.Ticker(t)
        hist = stock.history(period="1d")

        price = hist["Close"].iloc[-1]
        open_price = hist["Open"].iloc[0]
        change = price - open_price

        rows.append([t, price, change])

    return pd.DataFrame(rows, columns=["Ticker", "Price", "Change"])