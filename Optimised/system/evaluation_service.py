from system.reviewer import Reviewer
import streamlit as st

class EvaluationService:
    def __init__(self, submission_repo, notification_service):
        self.submission_repo = submission_repo
        self.notification_service = notification_service

    def start_evaluation(self, submission_id, reviewer_names):
        reviewers = [Reviewer(name) for name in reviewer_names]
        scores = []

        for reviewer in reviewers:
            scores.append(reviewer.submit_score())

        average = self.calculate_average(scores)
        consensus = self.check_consensus(scores)
        decision = self.apply_rules(average, consensus)

        self.submission_repo.save_result(submission_id, decision)
        self.notification_service.notify(decision)

    def calculate_average(self, scores):
        avg = sum(scores) / len(scores)
        st.write(f"Average score: {avg:.2f}")
        return avg

    def check_consensus(self, scores):
        return max(scores) - min(scores) <= 30

    def apply_rules(self, avg, consensus):
        if avg >= 75 and consensus:
            return "ACCEPTED"
        elif avg < 50:
            return "REJECTED"
        return "REVISION"