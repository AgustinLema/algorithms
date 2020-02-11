class HashMap():
    def __init__(self, size):
        self.buckets = [[] for _ in range(size)]
        self.n_buckets = size

    def get(self, key, default=None):
        h = self.hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                return v
        return default

    def set(self, key, value):
        h = self.hash(key)
        for i in range(len(self.buckets[h])):
            if key == self.buckets[h][i][0]:
                self.buckets[h][i] = (key, value)
                return
        self.buckets[h].append((key, value))

    def hash(self, key):
        return hash(key) % self.n_buckets
