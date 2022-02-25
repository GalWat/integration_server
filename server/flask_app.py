from flask import Flask, request
import git

from triggers.hook_trigger_service import HookTriggerService
from triggers.polling_trigger_service import PollingTriggerService
from jobs.job_service import JobService

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

    hook_trigger_service.invoke_trigger(service, data)


@app.route('/update_server', methods=['POST'])
def update_hook():
    if request.method == 'POST':
        repo = git.Repo('/home/GalWat')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400