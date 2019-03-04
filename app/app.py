from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response
from pymongo import MongoClient
from OpenSSL import SSL

from entities.container import container
from models.record import record
from models.signature import signature

# context = SSL.Context(SSL.PR .PROTOCOL_TLSv1_2)
# context.use_privatekey_file('pki/private.key')
# context.use_certificate_file('pki/certificate.pem')

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
    check = signature()
    if 'Signature' in request.headers:
        verify = check.verify(signature, request.json)
        if (verify == False):
            record_merged = {'result': 'wrong signature', 'event': request.json, 'headers': dict(request.headers)}
            model.save(wh_id, record_merged)
            return jsonify({'result': 'OK'})
    record_merged = {'event': request.json, 'headers' : dict(request.headers)}
    model.save(wh_id, record_merged)
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
    return jsonify(item)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
