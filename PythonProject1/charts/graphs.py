import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

from config.settings import STOCKS
from config.settings import color_map

st.subheader("📈 Multi-Stock Chart")


col1, col2, col3 = st.columns(3)

with col1:
    t1 = st.selectbox("Stock 1", STOCKS, index=0)
with col2:
    t2 = st.selectbox("Stock 2", STOCKS, index=1)
with col3:
    t3 = st.selectbox("Stock 3", STOCKS, index=2)

time_range = st.selectbox(
    "Time Range",
    ["1d", "5d", "1mo", "3mo", "6mo"]
)

def show_chart(ticker):
    df = yf.download(ticker, period=time_range, interval="1h")
    return df

fig = go.Figure()

for ticker in [t1, t2, t3]:
    df = show_chart(ticker)

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name=f"{ticker} Stock",
            line=dict(color=color_map.get(STOCKS))
        )
    )

fig.update_layout(
    title="Multi-Stock Price Comparison",
    xaxis_title="Time",
    yaxis_title="Price (USD)",
    template="plotly_dark",
    legend_title="Stocks"
)

st.plotly_chart(fig, use_container_width=True)