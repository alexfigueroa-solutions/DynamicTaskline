# StatusRenderer class to render the status of tasks.
class StatusRenderer:
    def __init__(self, output_stream_manager):
        self.output_stream_manager = output_stream_manager

    def render(self, status):
        self.output_stream_manager.write(status)
