import streamlit as st

def show_chart(df):
    st.subheader("📈 Price Chart")

    st.line_chart(df.set_index("Ticker")["Price"])