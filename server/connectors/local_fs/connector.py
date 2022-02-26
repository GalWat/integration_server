import json


class LocalFSConnector:
    def __init__(self):
        pass

    def read_json(self, file_name: str) -> dict:
        with open(file_name, 'r') as file_in:
            result = json.loads(file_in.read())
        return result

    def write_json(self, file_name: str, data: dict) -> None:
        with open(file_name, 'w') as file_out:
            file_out.write(json.dumps(data))
