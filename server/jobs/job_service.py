import importlib
import warnings

from pathlib import Path

from .trigger_types import HookTrigger, PollingTrigger


class JobService:
    def __init__(self, hook, polling):
        self.hook_trigger_service = hook
        self.polling_trigger_service = polling

        self.jobs = []

        p = Path('')

        for item in p.glob('**/jb_*.py'):
            if not item.is_file():
                continue

            print(item)

            job = importlib.import_module(f'{".".join(item.parts[:-1])}.{item.stem}')
            self.jobs.append(job)

        for job in self.jobs:
            job_object = job.Job()

            for trigger in job_object.triggers:
                if isinstance(trigger, HookTrigger):
                    self.hook_trigger_service.create_trigger(trigger, job_object)
                elif isinstance(trigger, PollingTrigger):
                    self.polling_trigger_service.create_trigger(trigger)
                else:
                    warnings.warn(f'trigger has unexpected type: {job} - {trigger}')
