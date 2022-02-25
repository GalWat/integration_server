from connectors import LocalFSConnector
from . import Statuses


class UpdateStatus:
    triggers = [{'type': 'hook', 'service_name': 'status', 'methods': ['POST']}]

    def __init__(self):
        self.local_fs = LocalFSConnector()

    def execute(self, data: dict) -> None:
        current_state = self.local_fs.read_json('status.json')
        current_state[data['person']] = Statuses.__getattr__(data['status']).value

        self.local_fs.write_json('status.json', current_state)
