from server.triggers import HookTrigger
from loguru import logger


class Job:
    triggers = [HookTrigger(service_name='alice', methods=['POST'])]

    def execute(self, data: dict) -> str:
        logger.info(f"Alice request: {data}")
        return "OK"
