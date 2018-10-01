# -*- coding: utf-8 -*-
from models.search_result import search_result

class record():

    db = None

    def __init__(self, container):
        self.db = container.get('db')

    def save(self, result):
        self.db.search_results.insert_one(result)

    def list(self):
        output = []
        for q in self.db.search_results.find({}, {"_id": 0}):
            output.append(q)
        return output

    def get_by_id(self, id):
        item = self.db.search_results.find_one({'service_id': id}, {"_id": 0})
        return item
