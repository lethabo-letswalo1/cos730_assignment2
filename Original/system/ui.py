from system.submission_controller import SubmissionController

class UI:
    def __init__(self):
        self.submission_controller = SubmissionController()

    def submit_research_output(self, data):
        self.submission_controller.submit(data)