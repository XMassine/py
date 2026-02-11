import time
from pymemcache.client import base
from lru import LRU


class Mem:
    def __init__(self, host="localhost", port=11211, capacity=5):
        self.client = base.Client((host, port))
        self.lru = LRU(capacity)

    def create(self, key, data):
        removed_keys = self.lru.create(key)

        # Remove evicted keys from memcached
        for k in removed_keys:
            self.client.delete(k)

        start = time.perf_counter()
        self.client.set(key, data)
        return time.perf_counter() - start

    def read(self, key):
        start = time.perf_counter()
        data = self.client.get(key)
        elapsed = time.perf_counter() - start

        if data:
            self.lru.read(key)

        return data, elapsed

    def delete(self, key):
        self.lru.delete(key)
        self.client.delete(key)
