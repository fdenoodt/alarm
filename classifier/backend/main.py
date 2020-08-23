import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from alarm import Alarm
from datetime import datetime
from set_interval import SetInterval
from config_manager import ConfigManager

app = Flask(__name__)
CORS(app)

alarm = Alarm()


def tick():
    alarm.verify_alarm()


@app.route('/', methods=['GET', 'POST'])
def set_alarm():
    logging.basicConfig(level=logging.DEBUG)

    if request.method == 'GET':
        return jsonify(hour=alarm.hour,
                       minute=alarm.minute)

    if request.method == 'POST':
        hour = int(request.form.get("hour", None))
        minute = int(request.form.get("minute", None))

        alarm.set_alarm(hour, minute)
        return jsonify(hour=hour,
                       minute=minute)


@app.route('/time', methods=['GET'])
def get_time():
    logging.basicConfig(level=logging.DEBUG)
    d = datetime.now()
    hour = d.hour
    minute = d.minute

    return jsonify(hour=hour,
                   minute=minute)


@app.route('/inTimeWindow', methods=['GET'])
def get_in_time_window():
    logging.basicConfig(level=logging.DEBUG)
    in_time = alarm.in_time_window(None, None)
    return jsonify(inTimeWindow=in_time)


def init():
    t = SetInterval(2, tick)
    t.start()

    if ConfigManager.get_config()['production'] == 'True':
        app.run(host='0.0.0.0')
    else:
        app.run()


init()
