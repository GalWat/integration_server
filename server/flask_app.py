from flask import Flask, request
import git

from workers import StatusesWorker

app = Flask(__name__)

statuses_worker = StatusesWorker()


@app.route('/')
def processing():
    return 'OK'


@app.route('/status', methods=['GET'])
def get_status():
    person = request.args.get('person')

    if person:
        return statuses_worker.get_status(person)

    return ' | '.join(statuses_worker.all_statuses())


@app.route('/status', methods=['POST'])
def change_status():
    data = request.json
    statuses_worker.change_status(data['person'], data['status'])
    return "OK"


@app.route('/telegram', methods=['POST'])
def telegram_request():
    pass


@app.route('/update_server', methods=['POST'])
def update_webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/GalWat')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400