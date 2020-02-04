from data_structures.queue import Queue
from data_structures.stack import Stack
from data_structures.deque import Deque
from data_structures.linked_list import LinkedList, DoubleLinkedList
from data_structures.linked_queue import LinkedQueue
from data_structures.linked_stack import LinkedStack
from data_structures.binary_search_tree import BinarySearchTree


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


def test_deque():
    d = Deque(10)
    for num in range(1, 5):
        d.push(num)

    assert d.pop() == 4
    for num in range(4, 10):
        d.push(num)

    d.push_left(0)
    numbers = [d.pop_left() for i in range(10)]
    assert numbers == list(range(10))


def test_linked_list():
    ll = LinkedList()
    for num in range(5):
        ll.insert(num)

    assert ll.to_list() == list(range(5))[::-1]
    ll.insert_in_pos(5, -1)
    assert ll.to_list() == list(range(-1, 5))[::-1]
    ll.remove(ll.get_node(3))
    assert ll.to_list() == [4, 3, 2, 0, -1]
    ll.delete_pos(3)
    assert ll.to_list() == [4, 3, 2, -1]


def test_dobule_linked_list():
    dll = DoubleLinkedList()
    for num in range(5):
        dll.insert(num)

    assert dll.to_list() == list(range(5))[::-1]
    dll.insert_in_pos(5, -1)
    assert dll.to_list() == list(range(-1, 5))[::-1]
    dll.remove(dll.get_node(3))
    assert dll.to_list() == [4, 3, 2, 0, -1]
    dll.delete_pos(3)
    assert dll.to_list() == [4, 3, 2, -1]


def test_linked_queue():
    q = LinkedQueue()
    for num in range(5):
        q.enqueue(num)

    assert q.dequeue() == 0
    for num in range(5, 11):
        q.enqueue(num)

    numbers = [q.dequeue() for i in range(10)]
    assert numbers == list(range(1, 11))


def test_linked_stack():
    s = LinkedStack()
    for num in range(5):
        s.push(num)

    assert s.pop() == 4
    for num in range(5, 11):
        s.push(num)

    numbers = [s.pop() for i in range(10)]
    assert numbers == [10, 9, 8, 7, 6, 5, 3, 2, 1, 0]

def test_binary_search_tree():
    bst = BinarySearchTree()
    numbers = [9, 1, 52, 5, 11, 523, 7, 1, 0, -5, 42, 3, 57]
    sorted_numbers = sorted(numbers)
    bst.insert_list(numbers)
    assert bst.get_sorted_list() == sorted(numbers)
    assert bst.search(sorted_numbers[5])['value'] == 5
    assert bst.minimum()['value'] == min(numbers)
    assert bst.maximum()['value'] == max(numbers)
    assert bst.predecessor(bst.search(sorted_numbers[4]))['value'] == sorted_numbers[3]
    assert bst.successor(bst.search(sorted_numbers[4]))['value'] == sorted_numbers[5]
    bst.remove(numbers[4])
    assert bst.get_sorted_list() == sorted_numbers.remove(numbers[4])
