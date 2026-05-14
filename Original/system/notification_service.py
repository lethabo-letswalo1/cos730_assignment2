import streamlit as st

class NotificationService:
    def notify_acceptance(self):
        st.success("Paper Accepted")

    def notify_rejection(self):
        st.error("Paper Rejected")

    def notify_revision(self):
        st.warning("Revision Required")

    def send_notification(self):
        st.info("Notification sent to researcher")