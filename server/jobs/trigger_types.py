class HookTrigger:

    def __init__(self, service_name, methods):
        self.service_name = service_name
        self.methods = methods
        self.job = None


class PollingTrigger:
    def __init__(self):
        pass  # Not implemented
