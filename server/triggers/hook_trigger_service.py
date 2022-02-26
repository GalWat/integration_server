class HookTriggerService:
    def __init__(self):
        self.triggers = {}

    def add_trigger(self, trigger):
        if not self.triggers.get(trigger.service_name):
            self.triggers[trigger.service_name] = {}

        for method in trigger.methods:
            self.triggers[trigger.service_name][method] = trigger

    def invoke_trigger(self, service_name, method, data):
        trigger = self.triggers.get(service_name)
        trigger = trigger.get(method) if trigger else None
        if not trigger:
            return None

        response = trigger.invoke(data)
        if response:
            return response
