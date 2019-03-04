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
@app.route('/wh', methods=['GET'])
@app.route('/wh/', methods=['GET'])
def get_all():
    output = model.list_buckets()
    return jsonify({'Webhooks': output})

# Webhooks
@app.route('/wh/<string:wh_id>', methods=['POST'])
def new_item(wh_id='default'):
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
    model.save(wh_id, record_merged)
    return jsonify({'result': 'OK', 'signature': signature_check})

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
    return jsonify(item)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
