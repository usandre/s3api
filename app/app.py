from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient

from entities.container import container
from models.record import record

app = Flask(__name__)

client = MongoClient( 'mongodb', 27017)
db = client.search_results

storage = container()
storage.set('db', db)

model = record(storage)

@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]
    return render_template('todo.html', items=items)


@app.route('/services', methods=['POST'])
def new():
    model.id = request.form['id']
    model.xml = request.form['xml']
    model.type = request.form['type']

    model.save()

    return redirect(url_for('todo'))

@app.route('/services/<string:id>', methods=['GET'])
def find_service(id):
    item = model.get(id)
    return jsonify({'result': item})

@app.route('/services', methods=['GET'])
def get_all():
    output = model.list()
    return jsonify({'result': output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)