import streamlit as st

class Validator:
    def validate_format(self, data):
        print("Validator: Validating submission format...")

        if data['content'].strip() == "":
            st.error("Validation failed.")
            return False

        st.success("Validation successful.")
        return True