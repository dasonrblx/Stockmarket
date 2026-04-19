import streamlit as st

from config.settings import STOCKS
from auth.login import login
from data.fetcher import get_stock_data
from charts.graphs import show_chart
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000, key="refresh")

st.set_page_config(page_title="Stock Dashboard", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:
    login()
    st.stop()

st.title("📊 Live Stock Dashboard")

stocks = st.multiselect("Select Stocks", STOCKS, default=STOCKS)

placeholder = st.empty()

df = get_stock_data(stocks)

with placeholder.container():
    st.dataframe(df)
    show_chart(df)
