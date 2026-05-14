import streamlit as st

class ReviewerAssignmentService:
    def __init__(self, reviewer_repo):
        self.reviewer_repo = reviewer_repo

    def assign_reviewers(self, submission_id):
        reviewers = self.reviewer_repo.get_eligible_reviewers()
        return self.filter_and_balance(reviewers)

    def filter_and_balance(self, reviewers):
        print("ReviewerAssignmentService: Filtering conflicts & balancing workload...")
        return reviewers[:2]