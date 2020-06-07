import logging
from flask import Flask, request
from alarm import Alarm
from set_interval import SetInterval

app = Flask(__name__)
alarm = Alarm()


def tick():
    alarm.verify_alarm()


@app.route('/', methods=['GET', 'POST'])
def set_alarm():
    logging.basicConfig(level=logging.DEBUG)

    if request.method == 'GET':
        return '{}:{}'.format(alarm.hour, alarm.minute)

    if request.method == 'POST':
        hour = int(request.form.get("hour", None))
        minute = int(request.form.get("minute", None))

        alarm.set_alarm(hour, minute)

        return 'alarm set'


def init():
    t = SetInterval(1, tick)
    t.start()

    app.run()


init()
