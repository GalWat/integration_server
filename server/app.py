from flask import Flask, request

from server.triggers.hook_trigger_service import HookTriggerService
from server.triggers.polling_trigger_service import PollingTriggerService
from server.jobs.job_service import JobService
from loguru import logger

app = Flask(__name__)

hook_trigger_service = HookTriggerService()
polling_trigger_service = PollingTriggerService()

job_service = JobService(hook=hook_trigger_service, polling=polling_trigger_service)


@app.route('/')
def processing():
    return 'OK'


@app.route('/triggers/<service>', methods=['POST', 'GET'])
def incoming_webhook_trigger(service):
    data = dict()

    if request.method == 'POST':
        data = request.json
    elif request.method == 'GET':
        data = request.args

    logger.info(f"Incoming request: {request.method} /triggers/{service} Data: {data}")

    response = hook_trigger_service.invoke_trigger(service, request.method, data)
    if response:
        return response


if __name__ == '__main__':
    app.run(
        port=8080,
        ssl_context='adhoc',
    )
