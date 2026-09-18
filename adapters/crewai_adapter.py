import io
from contextlib import redirect_stderr, redirect_stdout

from crewai.flow.flow import Flow, start

from adapters.common import submit_to_authority


class DeploymentFlow(Flow):
    def __init__(self, request: dict):
        super().__init__()
        self.request = request

    @start()
    def request_deployment(self):
        return submit_to_authority(self.request)


def run(request: dict) -> dict:
    # CrewAI's rich lifecycle display would drown out the cross-framework result table.
    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        return DeploymentFlow(request).kickoff()
