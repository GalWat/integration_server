from flask import abort


class HookTriggerService:
    def __init__(self):
        self.triggers = {}

    def create_trigger(self, trigger, job):
        if not self.triggers.get(trigger.service_name):
            self.triggers[trigger.service_name] = {}

        for method in trigger.methods:
            self.triggers[trigger.service_name][method] = job

    def invoke_trigger(self, service_name, method, data):
        trigger = self.triggers.get(service_name)
        job = trigger.get(method) if trigger else None
        if not trigger:
            abort(404)

        response = job.execute(data)
        if response:
            return response
