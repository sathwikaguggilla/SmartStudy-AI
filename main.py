import streamlit as st
from core.summarizer import summarize_text
from core.quiz import generate_quiz
from core.chatbot import chatbot_response
from utils.file_handler import extract_text_from_pdf
from components.sidebar import show_sidebar
from components.layout import show_title

# ✅ MUST be first Streamlit command
st.set_page_config(page_title="SmartStudy AI", layout="wide")

# Sidebar & Title
show_sidebar()
show_title()
text = ""

# Welcome Card
st.markdown("""
<div style="
background-color:#FFFFFF;
padding:25px;
border-radius:15px;
margin-bottom:20px;
box-shadow:0px 4px 10px rgba(0,0,0,0.05);
color:#1E293B;">
<h2>🚀 Welcome to SmartStudy AI</h2>
<p>Your AI-powered assistant for smarter learning.</p>
</div>
""", unsafe_allow_html=True)

# Upload Section Card
st.markdown("""
<div style="
background-color:#FFFFFF;
padding:20px;
border-radius:15px;
margin-bottom:20px;
box-shadow:0px 4px 10px rgba(0,0,0,0.05);
color:#1E293B;">
<h4>📄 Upload or Paste Study Notes</h4>
</div>
""", unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

# Text Area
text_input = st.text_area("Or paste your study notes here:")

if text_input:
    text = text_input

# ✅ Buttons Side by Side
col1, col2 = st.columns(2)

with col1:
    if st.button("✨ Generate Summary"):
        if text:
            summary = summarize_text(text)
            st.markdown("### 📌 Summary")
            st.success(summary)
        else:
            st.warning("Please upload or enter text.")

with col2:
    if st.button("📝 Generate Quiz"):
        if text:
            quiz = generate_quiz(text)
            st.markdown("### 🧠 Quiz Questions")

            for i, (q, a) in enumerate(quiz):
                st.markdown(f"""
<div style="
background-color:#FFFFFF;
padding:15px;
border-radius:12px;
margin-bottom:10px;
box-shadow:0px 2px 8px rgba(0,0,0,0.05);
color:#1E293B;">
<b>Q{i+1}:</b> {q}<br>
<b>Answer:</b> {a}
</div>
""", unsafe_allow_html=True)
        else:
            st.warning("Please upload or enter text.")

# Chatbot Section
st.markdown("""
<div style="background-color:#FFFFFF;
color:#1E293B;
box-shadow:0px 2px 8px rgba(0,0,0,0.05); padding:20px; border-radius:15px; margin-top:30px;">
<h2>🤖 Study Chatbot</h2>
</div>
""", unsafe_allow_html=True)

user_input = st.text_input("Ask something about your notes:")

if user_input:
    response = chatbot_response(user_input)
    st.info(response)

# Footer
st.markdown("---")
st.markdown("""
<center>
<p style="font-size:14px;">
© 2026 SmartStudy AI
</p>
</center>
""", unsafe_allow_html=True)