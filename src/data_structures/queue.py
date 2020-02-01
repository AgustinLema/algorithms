class Queue:
    def __init__(self, size):
        self.elements = [0] * size
        self.head = -1
        self.tail = 0

    def enqueue(self, element):
        self.elements[self.tail] = element
        self.tail += 1
        if self.tail >= len(self.elements):
            self.tail = 0

    def dequeue(self):
        self.head += 1
        if self.head >= len(self.elements):
            self.head = 0
        return self.elements[self.head]
