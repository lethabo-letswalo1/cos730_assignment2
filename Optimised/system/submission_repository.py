import streamlit as st

class SubmissionRepository:
    def __init__(self):
        self.submissions = {}
        self.results = {}

    def save_submission(self, data):
        submission_id = len(self.submissions) + 1
        self.submissions[submission_id] = data
        print(f"Saved submission {submission_id}")
        return submission_id

    def save_result(self, submission_id, result):
        self.results[submission_id] = result
        print(f"Saved result → {result}")

