import streamlit as st
from Langchain import get_qa_chain, create_vector_db
def app():
    st.title("E-shiskya Q&A ")
    btn = st.button("Create Vector Data")
    if btn:
        create_vector_db()

    question = st.text_input("Question: ")

    if question:
        chain = get_qa_chain()
        response = chain(question)

        st.header("Answer")
        st.write(response["result"])






