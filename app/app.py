from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response
from pymongo import MongoClient
from OpenSSL import SSL

from entities.container import container
from models.record import record
from models.signature import signature

app = Flask(__name__)

client = MongoClient( 'mongodb', 27017)

storage = container()
storage.set('db', client.subscriptions)

model = record(storage)

@app.route('/')
def default():
    return jsonify({'open': 'OK'})

# LISTING
@app.route('/sub', methods=['GET'])
@app.route('/sub/', methods=['GET'])
def get_all():
    output = model.list_buckets()
    return jsonify(output)

# Webhooks
@app.route('/sub/<string:sub_id>', methods=['POST'])
def new_item(sub_id='default'):
    check = signature()
    signature_check = 'not present'
    if 'Concur-Signature' in request.headers:
        header_signature = request.headers['Concur-Signature']
        verify = check.verify(header_signature, request.data)
        if (verify == False):
            signature_check = 'invalid'
        else:
            signature_check = 'valid'
    record_merged = {'signature': signature_check,'event': request.json, 'headers' : dict(request.headers)}
    model.save(sub_id, record_merged)
    return jsonify({'result': 'OK', 'signature': signature_check})

@app.route('/sub/<string:sub_id>', methods=['GET'])
@app.route('/sub/<string:sub_id>/', methods=['GET'])
def webhook_content(sub_id):
    output = model.bucket_list(sub_id)
    if output is None:
        return jsonify({'result' : 'not found'}), 404
    return jsonify(output)

@app.route('/sub/<string:sub_id>', methods=['DELETE'])
def webhook_delete(sub_id):
    output = model.collection_delete(sub_id)
    if output is None:
        return jsonify({'result' : 'not found'}), 404
    return jsonify({'Webhook [' + sub_id + '] dropped ': output})


# Webhook items
@app.route('/sub/<string:sub_id>/<string:id>', methods=['GET'])
def find_service(sub_id, id):
    item = model.get_by_id(sub_id, id)
    if item is None:
        return jsonify({'result' : 'not found'}), 404
    return jsonify(item)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
