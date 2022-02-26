from enum import Enum


class Statuses(Enum):
    DEFAULT = "Не занят"
    BUSY = "Занят"
    READY_FOR_TALK = "Хочу общаться"
    DO_NOT_DISTURB = "Не пиши"
    ERROR = "Ошибка"
