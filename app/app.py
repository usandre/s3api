from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response
from pymongo import MongoClient

from entities.container import container
from models.record import record

app = Flask(__name__)

client = MongoClient( 'mongodb', 27017)

storage = container()
storage.set('db', client.subscriptions)

model = record(storage)

@app.route('/')
def default():
    output = model.list()
    return jsonify({'result': output})


@app.route('/wh/<string:sub_id>', methods=['POST'])
def new(sub_id='default'):
    model.save(sub_id, request.json)
    return jsonify({'result': 'OK'})

@app.route('/wh/<string:sub_id>', methods=['GET'])
def get_onelist(sub_id):
    output = model.list(sub_id)
    return jsonify({'Webhook ' + sub_id + ' items': output})

@app.route('/wh/<string:sub_id>/<int:id>', methods=['GET'])
def find_service(id):
    item = model.get_by_id(id)
    return jsonify({'result': item})

@app.route('/wh', methods=['GET'])
def get_all():
    output = model.list_buckets()
    return jsonify({'Webhooks': output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)