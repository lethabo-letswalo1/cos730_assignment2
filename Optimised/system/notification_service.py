import streamlit as st

class NotificationService:
    def notify(self, decision):
        if decision == "ACCEPTED":
            st.success("Paper Accepted")
        elif decision == "REJECTED":
            st.error("Paper Rejected")
        else:
            st.warning("Revision Required")