
from system.submission_service import SubmissionService

class UI:
    def __init__(self):
        self.submission_controller = SubmissionService()

    def submit_research_output(self, data):
        self.submission_controller.submit(data)