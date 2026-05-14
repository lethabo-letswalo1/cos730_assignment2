import random
import streamlit as st

class Reviewer:
    def __init__(self, name):
        self.name = name
        
    def assign_review(self):
        print(f"{self.name}: Review assigned.")

    def submit_score(self, evaluation_manager):
        score = random.randint(0, 100)
        print(f"Reviewer ({self.name}): Submitting score {score} to EvaluationManager...")
        evaluation_manager.submit_score(score)