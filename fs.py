import os
import time


class FS:
    def __init__(self, root_dir="images"):
        self.root_dir = root_dir
        os.makedirs(root_dir, exist_ok=True)

    def list(self):
        return os.listdir(self.root_dir)

    def create(self, filename, data):
        path = os.path.join(self.root_dir, filename)
        start = time.perf_counter()
        with open(path, "wb") as f:
            f.write(data)
        return time.perf_counter() - start

    def read(self, filename):
        path = os.path.join(self.root_dir, filename)
        start = time.perf_counter()
        with open(path, "rb") as f:
            data = f.read()
        return data, time.perf_counter() - start

    def delete(self, filename):
        path = os.path.join(self.root_dir, filename)
        if os.path.exists(path):
            os.remove(path)
