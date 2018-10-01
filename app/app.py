from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response
from pymongo import MongoClient

from entities.container import container
from models.record import record

app = Flask(__name__)

client = MongoClient( 'mongodb', 27017)

storage = container()
storage.set('db', client.search_results)

model = record(storage)

@app.route('/')
def default():
    output = model.list()
    return jsonify({'result': output})


@app.route('/services', methods=['POST'])
def new():
    # @todo mmake service_id unique
    model.save(request.json)
    return jsonify({'result': 'OK'})

@app.route('/services/<int:id>', methods=['GET'])
def find_service(id):
    item = model.get_by_id(id)
    return jsonify({'result': item})

@app.route('/services', methods=['GET'])
def get_all():
    output = model.list()
    return jsonify({'result': output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)