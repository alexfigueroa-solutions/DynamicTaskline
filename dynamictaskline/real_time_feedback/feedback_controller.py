from .status_renderer import StatusRenderer

# FeedbackController class to control the feedback given to users.
class FeedbackController:
    def __init__(self, status_renderer):
        self.status_renderer = status_renderer

    def provide_feedback(self, message):
        self.status_renderer.render(message)
