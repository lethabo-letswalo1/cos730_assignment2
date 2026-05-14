import streamlit as st
from system.database import Database

class ReviewerManager:
    def get_available_reviewers(self):
        print("Getting available reviewers...")
        database = Database()
        reviewer_list = database.fetch_reviewers()
        reviewer_list = self.filter_conflicts(reviewer_list)
        filtered = self.check_workload(reviewer_list)
        return filtered

    def filter_conflicts(self, reviewer_list):
        print("Filtering conflicts...")
        return reviewer_list

    def check_workload(self, reviewer_list):
        print("Checking workload...")
        return reviewer_list