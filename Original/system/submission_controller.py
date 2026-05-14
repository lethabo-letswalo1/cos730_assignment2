import streamlit as st
from system.database import Database
from system.evaluation_manager import EvaluationManager
from system.reviewer import Reviewer
from system.reviewer_manager import ReviewerManager
from system.validator import Validator

class SubmissionController:
    def __init__(self):
        self.validator = Validator()
        self.database = Database()
        self.reviewer_manager = ReviewerManager()

    def submit(self, data):
        valid = self.validator.validate_format(data)

        if not valid:
            st.error("Submission rejected.")
            return

        confirmation = self.database.save_submission(data)
        print(f"{confirmation}")
        
        filtered_reviewers = self.reviewer_manager.get_available_reviewers()

        reviewers = []

        for reviewer_data in filtered_reviewers:
            print(f"{reviewer_data}")
            name = reviewer_data["name"]
            reviewer = Reviewer(name)
            reviewer.assign_review()
            reviewers.append(reviewer)

        self.evaluation_manager = EvaluationManager(reviewers)
        self.evaluation_manager.start_evaluation()
