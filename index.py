import streamlit as st

from streamlit_option_menu import option_menu

from PIL import Image

import pickle
from pathlib import Path

import streamlit_authenticator as stauth

# Loading Image using PIL
im = Image.open('logo.png')
import home, script, main, about
st.set_page_config(
        page_title="E-sikshya",  page_icon = im
)
names = ["Sumip Chaudhary","Yves Saint"]
usernames = ["Sumip","YSL"]
passwords = ["XXX","XXX"]
hashed_passwords = stauth.Hasher(passwords).generate()

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,"esya_dashboard", "abcdef", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    #main
    class MultiApp:

        def __init__(self):
            self.apps = []

        def add_app(self, title, func):

            self.apps.append({
                "title": title,
                "function": func
            })

        def run():
            # app = st.sidebar(
            with st.sidebar:        
                app = option_menu(
                    menu_title='E-sikshya ',
                    options=['Home','ChatPdf','Chat-Bot','About'],
                    icons=['house-fill','book-half','chat-fill','info-circle-fill'],
                    menu_icon='chat-text-fill',
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important","background-color":'black'},
            "icon": {"color": "white", "font-size": "23px"}, 
            "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},}
                    
                    )

            
            if app == "Home":
                home.app()
            if app == "ChatPdf":
                script.main()
            if app == "Chat-Bot":
                main.app()
            if app == "About":
                about.app()
        
                
            
                
        run()            
            
