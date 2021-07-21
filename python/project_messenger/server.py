import time
from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def Hello():
    return 'Hello, World!'


@app.route('/status')
def status():
    return {
        'status': True,
        'name': 'Messenger',
        'time1' : time.time(),
        'time2' : datetime.now()
    }


app.run()
