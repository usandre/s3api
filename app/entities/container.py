class container():
    data = {}

    def set(self, name, obj):
        self.data[name] = obj

    def get(self, name):
        res = None

        if name in self.data:
            res = self.data[name]

        return res
