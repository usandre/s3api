# -*- coding: utf-8 -*-

class record():

    db = None

    def __init__(self, container):
        self.db = container.get('db')

    def save(self, collection_id, result):
        self.db[collection_id].insert_one(result)

    def list_buckets(self):
        return self.db.list_collection_names()

    def bucket_list(self, collection_id):
        if collection_id not in self.db.list_collection_names():
            return None
        output = []
        for q in self.db[collection_id].find({}, {"_id": 0}):
            output.append(q)
        return output

    def collection_delete(self, collection_id):
        if collection_id in self.db.list_collection_names():
            result = self.db[collection_id].drop()
        else:
            return None
        return True

    def get_by_id(self, collection_id, id):
        item = self.db[collection_id].find_one({"event.id" : id}, {"_id": 0})
        if item is None:
            item = self.db[collection_id].find_one({"event.correlationId": id}, {"_id": 0})
        return item
