from data_structures.linked_list import LinkedList


class LinkedStack:
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, element):
        self.linked_list.insert(element)

    def pop(self):
        node = self.linked_list.get_node(0)
        self.linked_list.remove(node)
        return node["value"]
