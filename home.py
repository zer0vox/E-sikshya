import streamlit as st
def app():
    # Set page title and favicon
   
    st.image('logo.png')
    # Add a header
    st.header("Welcome to E-sikshya!")

    # Add some text
    st.write("This is a simple web-app built with Streamlit. You can use it to interact with your pdf or chat with our intelligent bot.")
    st.write("Documentation for the project is provided below. Also source code is available at my github.")
  

    # Add some links
    st.markdown("[GitHub](https://github.com/zer0vox), [LinkedIn](https://linkedin.com/in/username), [Twitter](https://twitter.com/username)", unsafe_allow_html=True)

   

  