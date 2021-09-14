from enum import Enum


class Statuses(Enum):
    DEFAULT = "Не занят"
    BUSY = "Занят"
    READY_FOR_TALK = "Хочу общаться"
    DO_NOT_DISTURB = "Не пиши"
    ERROR = "Ошибка"


class StatusesWorker:
    def __init__(self):
        self.statuses = {
            'misha': Statuses.DEFAULT,
            'sveta': Statuses.DEFAULT
        }

    def all_statuses(self):
        return [f'{key}: {value.value}' for key, value in self.statuses.items()]

    def get_status(self, person):
        return self.statuses.get(person, Statuses.ERROR).value

    def change_status(self, person, status):
        self.statuses[person] = status
