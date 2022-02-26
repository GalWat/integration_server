# from enum import Enum
#
#
# class Statuses(Enum):
#     DEFAULT = "Не занят"
#     BUSY = "Занят"
#     READY_FOR_TALK = "Хочу общаться"
#     DO_NOT_DISTURB = "Не пиши"
#     ERROR = "Ошибка"
#

class HookTrigger:

    def __init__(self, service_name, methods):
        self.service_name = service_name
        self.methods = methods
        self.job = None

    def attach_job(self, job):
        self.job = job

    def invoke(self, data):
        response = self.job.execute(data)
        if response:
            return response
