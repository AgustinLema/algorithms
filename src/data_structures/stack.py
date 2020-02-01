class Stack:
    def __init__(self, size):
        self.elements = [0] * size
        self.tail = 0

    def push(self, element):
        self.elements[self.tail] = element
        self.tail += 1
        if self.tail >= len(self.elements):
            self.tail = 0

    def pop(self):
        self.tail -= 1
        if self.tail < 0:
            self.tail = len(self.elements) - 1
        return self.elements[self.tail]
