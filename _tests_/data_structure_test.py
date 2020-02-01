from data_structures.queue import Queue
from data_structures.stack import Stack


def test_queue():
    q = Queue(10)
    for num in range(5):
        q.enqueue(num)

    assert q.dequeue() == 0
    for num in range(5, 11):
        q.enqueue(num)

    numbers = [q.dequeue() for i in range(10)]
    assert numbers == list(range(1, 11))


def test_stack():
    s = Stack(10)
    for num in range(5):
        s.push(num)

    assert s.pop() == 4
    for num in range(5, 11):
        s.push(num)

    numbers = [s.pop() for i in range(10)]
    assert numbers == [10, 9, 8, 7, 6, 5, 3, 2, 1, 0]