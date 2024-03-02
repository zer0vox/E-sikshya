import pickle
from pathlib import Path

import streamlit_authenticator as stauth
#this page was made for authentication but later merged to index.py
names = ["Sumip Chaudhary","Yves Saint"]
usernames = ["Sumip","YSL"]
passwords = ["XXX","XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "esya_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")