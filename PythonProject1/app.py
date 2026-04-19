import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from config.settings import color_map

st.subheader("📈 Stock Comparison Chart")

STOCKS = ["NVDA", "AAPL", "TSLA", "MSFT", "AMZN", "NQ=F"]

selected = st.multiselect(
    "Select up to 2 stocks",
    STOCKS,
    default=["NVDA"]
)

time_range = st.selectbox("Time Range", ["1d", "5d", "1mo", "3mo", "6mo"])

@st.cache_data
def load_data(ticker, time_range):
    return yf.download(ticker, period=time_range, interval="1h")

fig = go.Figure()

for ticker in selected:
    df = load_data(ticker, time_range)

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name=ticker,
            line=dict(color=color_map.get(ticker, "#ffffff"), width=3)
        )
    )

fig.update_layout(
    template="plotly_dark",
    title="Stock Comparison (Max 2 Selected)",
    xaxis_title="Time",
    yaxis_title="Price (USD)",
    legend_title="Selected Stocks"
)

st.plotly_chart(fig, use_container_width=True)