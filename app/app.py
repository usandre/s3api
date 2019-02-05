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
    return jsonify({'open': '/wh/'})

# LISTING
@app.route('/wh', methods=['GET'])
@app.route('/wh/', methods=['GET'])
def get_all():
    output = model.list_buckets()
    return jsonify({'Webhooks': output})

# Webhooks
@app.route('/wh/<string:wh_id>', methods=['POST'])
def new_item(wh_id='default'):
    model.save(wh_id, request.json)
    return jsonify({'result': 'OK'})

@app.route('/wh/<string:wh_id>', methods=['GET'])
@app.route('/wh/<string:wh_id>/', methods=['GET'])
def webhook_content(wh_id):
    output = model.bucket_list(wh_id)
    return jsonify({'Webhook [' + wh_id + '] items': output})

@app.route('/wh/<string:wh_id>', methods=['DELETE'])
def webhook_delete(wh_id):
    output = model.collection_delete(wh_id)
    return jsonify({'Webhook [' + wh_id + '] items': output})


# Webhook items
@app.route('/wh/<string:wh_id>/<string:id>', methods=['GET'])
def find_service(wh_id, id):
    item = model.get_by_id(wh_id, id)
    return jsonify({'result': item})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)