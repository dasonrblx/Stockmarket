import streamlit as st

USERS = {
    "admin": "5881",
    "Grace": "GraceOunh",
    "Patrick": "PatrickNdukwe",
}

def login():
    st.title("🔐 Login")

    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")

    if st.button("Login"):
        if user in USERS and USERS[user] == pw:
            st.session_state.logged_in = True
        else:
            st.error("Wrong credentials")