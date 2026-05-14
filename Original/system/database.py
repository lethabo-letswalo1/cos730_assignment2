import streamlit as st

class Database:
    def __init__(self):
        self.reviewer_list = [
            { "name": "Reviewer A" },
            { "name": "Reviewer B" },
            { "name": "Reviewer C" },
            { "name": "Reviewer D" }
        ]
        self.scores = []
            
    def save_submission(self, data):
        print(f"Database: Saving submission... {data['title']}")
        return "confirmation"

    def fetch_reviewers(self):
        print("Database: Fetching reviewers...")
        return self.reviewer_list

    def save_score(self, score):
        print(f"Database: Saving score {score}")
        self.scores.append(score)