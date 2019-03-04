# -*- coding: utf-8 -*-

class record():

    db = None

    def __init__(self, container):
        self.db = container.get('db')

    def save(self, sub_id, result):
        self.db[sub_id].insert_one(result)

    def list_buckets(self):
        return self.db.list_collection_names()

    def bucket_list(self, sub_id):
        output = []
        for q in self.db[sub_id].find({}, {"_id": 0}):
            output.append(q)
        return output

    def collection_delete(self,collection_id):
        result = self.db[collection_id].drop()
        return {'deleted': 'ok'}

    def get_by_id(self, wh_id, id):
        item = self.db[wh_id].find_one({}, {"_id": 0})
        return item
