from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    def post_request(self, url, headers, data):
        r = requests.post(url, headers=headers, json=data)
        return r

    def get_request(self, url, headers, params):
        r = requests.get(url, headers=headers, params=params)
        return r