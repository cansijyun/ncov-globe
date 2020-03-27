from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from scraper import main_scraper
import json
import random

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/nation')
@cross_origin()
def get_ncov_data_nation():
    with open('final/confirmedByNation.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return jsonify(data)


@app.route('/state')
@cross_origin()
def get_ncov_data_state():
    with open('final/confirmedByState.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/state-info-api')
@cross_origin()
def get_state_info_api():
    with open('mid/byState.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/privince-info-api')
@cross_origin()
def get_privince_info_api():
    with open('mid/newProvinces.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/')
@cross_origin()
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


def scraper_interval():
    print("scraper run")
    try:
        main_scraper()
    except Exception as e:
        print(e)


sched = BackgroundScheduler(daemon=True)
sched.add_job(scraper_interval, 'interval', minutes=120)
sched.start()
atexit.register(lambda: sched.shutdown())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
