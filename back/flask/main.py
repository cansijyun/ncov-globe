import requests
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json
import random



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'




@app.route('/nation')
@cross_origin()
def get_ncov_data_nation():
    with open('static/byState.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)
        data_nation = []
        num = []
        for item in data['areas']:
            num.append(item['totalConfirmed'])
        max_num = max(num)
        # print("Type:", max_num)

        for item in data['areas']:
            data_nation.append(item['lat'])
            data_nation.append(item['long'])
            item_num = (item['totalConfirmed'] / max_num) *1.3
            item_num = float("%.4f" % item_num)

            data_nation.append(item_num)
            data_nation.append(random.randint(0, 11))
    return jsonify(data_nation)


@app.route('/state')
@cross_origin()
def get_ncov_data_state():
    with open('final/confirmedByState.json', encoding="UTF-8") as json_file:
        data = json.load(json_file)

    return jsonify(data)



@app.route('/')
@cross_origin()
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
