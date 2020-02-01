from data_structures.linked_list import LinkedList


class LinkedQueue:
    def __init__(self):
        self.linked_list = LinkedList()
        self.last_node = None

    def enqueue(self, element):
        if self.last_node is None:
            self.linked_list.insert(element)
            self.last_node = self.linked_list.get_node(0)
        else:
            new_node = self.linked_list._make_node(element, None)
            self.last_node['next'] = new_node
            self.last_node = new_node

    def dequeue(self):
        node = self.linked_list.get_node(0)
        self.linked_list.remove(node)
        return node["value"]
