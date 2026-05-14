import streamlit as st
from system.ui import UI

st.title("Intelligent Submission and Review System")
st.subheader("Task 1 - Baseline Implementation")

title = st.text_input("Research Title")
content = st.text_area("Research Content")

data = {
    "title": title,
    "content": content
}

submit_btn = st.button("Submit Research Output")

if submit_btn:
    ui = UI()
    ui.submit_research_output(data)