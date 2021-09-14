from flask import Flask, request, json
import git

from statuses_worker import Statuses, StatusesWorker

app = Flask(__name__)

statuses_worker = StatusesWorker()


@app.route('/')
def processing():
    return "OK"


@app.route('/status', methods=['POST'])
def get_status():
    data = request.json
    return statuses_worker.get_status(data['person'])


@app.route('/change-status', methods=['POST'])
def change_status():
    data = request.json
    statuses_worker.change_status(data['person'], Statuses(data['status']))
    return "OK"


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/pythonevenings/repo')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400