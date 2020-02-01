class Deque:
    def __init__(self, size):
        self.elements = [0] * size
        self.head = size - 1
        self.tail = 0

    def push(self, element):
        self.elements[self.tail] = element
        self.tail += 1
        if self.tail >= len(self.elements):
            self.tail = 0

    def push_left(self, element):
        self.elements[self.head] = element
        self.head -= 1
        if self.head < 0:
            self.head = len(self.elements) - 1

    def pop(self):
        self.tail -= 1
        if self.tail < 0:
            self.tail = len(self.elements) - 1
        return self.elements[self.tail]

    def pop_left(self):
        self.head += 1
        if self.head >= len(self.elements):
            self.head = 0
        return self.elements[self.head]
