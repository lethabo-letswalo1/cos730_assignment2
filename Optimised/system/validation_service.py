import streamlit as st

class ValidationService:
    def validate(self, data):
        print("ValidationService: Validating submission...")
        if not data["content"].strip():
            return False, "Content cannot be empty"
        return True, None