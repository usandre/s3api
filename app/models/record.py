# -*- coding: utf-8 -*-
from models.search_result import search_result

class record():

    id = ''
    xml = ''
    type = ''

    db = None

    def __init__(self, container):
        self.db = container.get('db')

    def save(self):
        self.db.search_results.insert_one(self.map())

    def map(self):
        res = {
            'id' : self.id,
            'xml' : self.xml,
            'type': self.type
        }
        return res

    def list(self):
        output = []
        for q in self.db.search_results.find({}, {"_id": 0}):
            output.append(q)
        return output

    def get(self, id):
        item = self.db.search_results.find_one({'id': id}, {"_id": 0})
        return item
