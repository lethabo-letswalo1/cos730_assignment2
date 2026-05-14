import streamlit as st
from system.database import Database
from system.notification_service import NotificationService

class EvaluationManager:
    def __init__(self, reviewers):
        self.database = Database()
        self.notification_service = NotificationService()
        self.reviewers = reviewers

        self.scores = []
        self.average = 0.0
        self.consensus = False

    def submit_score(self, score):
        print(f"EvaluationManager: Receiving score {score}...")
        self.scores.append(score)
        self.database.save_score(score)

    def start_evaluation(self):
        print("EvaluationManager: Starting evaluation...")
        self.scores = []
        self.average = 0.0
        self.consensus = False

        for reviewer in self.reviewers:
            reviewer.submit_score(self)

        self.average = self.calculate_average()
        self.consensus = self.check_consensus()
        result = self.apply_rules()

        if result == "accepted":
            self.notification_service.notify_acceptance()
        elif result == "rejected":
            self.notification_service.notify_rejection()
        else:
            self.notification_service.notify_revision()
        self.notification_service.send_notification()

    def calculate_average(self):
        print("EvaluationManager: Calculating average...")
        if not self.scores:
            return 0.0
        avg = sum(self.scores) / len(self.scores)
        st.write(f"Average Score: {avg:.2f}")
        return avg

    def check_consensus(self):
        print("EvaluationManager: Checking consensus...")
        return True

    def apply_rules(self):
        print("EvaluationManager: Applying rules...")

        if self.average >= 75 and self.consensus:
            return "accepted"
        elif self.average < 50:
            return "rejected"
        else:
            return "revision"