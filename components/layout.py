import streamlit as st

def show_title():
    st.markdown("""
        <h1 style='text-align: center; color: #6C63FF;'>
        📚 SmartStudy AI
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: center; font-size:18px;'>
        Upload notes or paste text to generate summary, quizzes & chatbot assistance.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")