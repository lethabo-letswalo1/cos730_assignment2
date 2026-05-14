from system.notification_service import NotificationService
from system.reviewer_repository import ReviewerRepository
from system.evaluation_service import EvaluationService
from system.reviewer_assignment_service import ReviewerAssignmentService
from system.submission_repository import SubmissionRepository
from system.validation_service import ValidationService
import streamlit as st

class SubmissionService:
    def __init__(self):
        self.validation = ValidationService()
        self.submission_repo = SubmissionRepository()
        self.reviewer_repo = ReviewerRepository()
        self.assignment_service = ReviewerAssignmentService(self.reviewer_repo)
        self.notification_service = NotificationService()
        self.evaluation_service = EvaluationService(
            self.submission_repo, self.notification_service
        )

    def submit(self, data):
        valid, error = self.validation.validate(data)
        if not valid:
            st.error(error)
            return

        submission_id = self.submission_repo.save_submission(data)
        reviewers = self.assignment_service.assign_reviewers(submission_id)
        self.evaluation_service.start_evaluation(submission_id, reviewers)
