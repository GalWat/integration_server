from server.connectors import LocalFSConnector
from ..trigger_types import HookTrigger
from pathlib import Path

from . import Statuses


class Job:
    triggers = [HookTrigger(service_name='status', methods=['POST'])]

    def __init__(self):
        self.local_fs = LocalFSConnector()

    def execute(self, data: dict) -> str:
        file = Path('status.json')

        if file.is_file():
            current_state = self.local_fs.read_json(str(file))
        else:
            current_state = {}

        current_state[data['person']] = Statuses.__getattr__(data['status']).value

        self.local_fs.write_json('status.json', current_state)

        return 'OK'
