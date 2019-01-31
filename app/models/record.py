# -*- coding: utf-8 -*-
from models.search_result import search_result

class record():

    db = None

    def __init__(self, container):
        self.db = container.get('db')

    def save(self, sub_id, result):
        self.db[sub_id].insert_one(result)

    def list_buckets(self):
        return self.db.list_collection_names()

    def list(self, sub_id):
        output = []
        for q in self.db[sub_id].find({}, {"_id": 0}):
            output.append(q)
        return output

    def get_by_id(self, sub_id, id):
        item = self.db[sub_id].find_one({'service_id': id}, {"_id": 0})
        return item
