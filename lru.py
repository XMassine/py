from collections import OrderedDict


class LRU:
    def __init__(self, capacity=5, delete_count=1):
        self.capacity = capacity
        self.delete_count = delete_count
        self.cache = OrderedDict()

    def create(self, key):
        removed = []

        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = True
        self.cache.move_to_end(key, last=False)

        while len(self.cache) > self.capacity:
            for _ in range(self.delete_count):
                if self.cache:
                    k, _ = self.cache.popitem(last=True)
                    removed.append(k)

        return removed

    def read(self, key):
        if key in self.cache:
            self.cache.move_to_end(key, last=False)

    def delete(self, key):
        if key in self.cache:
            self.cache.pop(key)

    def keys(self):
        return list(self.cache.keys())
