import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

from config.settings import STOCKS
from config.settings import color_map

st.subheader("📈 Stock Comparison")

selected = st.multiselect("Select stocks", STOCKS, default=["NVDA", "AAPL"])
time_range = st.selectbox("Time Range", ["1d", "5d", "1mo", "3mo", "6mo"])

fig = go.Figure()

for ticker in selected:
    df = yf.download(ticker, period=time_range, interval="1h")

    if df is None or df.empty:
        st.warning(f"No data for {ticker}")
        continue

    df = df.dropna()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name=ticker,
            line=dict(color=color_map.get(ticker, "#ffffff"), width=2)
        )
    )

fig.update_layout(
    template="plotly_dark",
    title="Multi-Stock Comparison",
    xaxis_title="Time",
    yaxis_title="Price",
    legend_title="Stocks"
)

st.plotly_chart(fig, use_container_width=True)