import streamlit as st
from send_email import send_email


with st.form(key="email_form"):
    st.header("Contact Us")
    email= st.text_input(label = "Your email address")
    topic = st.selectbox("What topics do you want to discuss?",["Job Inquiries","Project Proposals","Other"])
    msg = st.text_area(label = "Your message")
    button = st.form_submit_button()
    if button:
        send_email(email,msg,topic)
        st.info("your email was sent successfully") 