from server.connectors import LocalFSConnector
from ..trigger_types import HookTrigger
from . import Statuses


class Job:
    triggers = [HookTrigger(service_name='status', methods=['GET'])]

    def __init__(self):
        self.local_fs = LocalFSConnector()

    def execute(self, data: dict) -> str:
        current_state = self.local_fs.read_json('status.json')

        if data.get('person'):
            return current_state.get(data['person'], Statuses.ERROR.value)
        else:
            return ' | '.join([f'{key}: {value}' for key, value in current_state.items()])
