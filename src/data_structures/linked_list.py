class LinkedList():
    def __init__(self):
        self.root = None

    def insert_in_pos(self, position, element):
        if position == 0:
            return self.insert(element)

        previous_node = self.get_node(position - 1)

        inserted_node = self._make_node(element, previous_node['next']) 
        previous_node['next'] = inserted_node

    def insert(self, element):
        self.root = self._make_node(element, self.root)

    def _make_node(self, element, next_node):
        return {
            "value": element,
            "next": next_node,
        }

    def get_node(self, position):
        node = self.root
        for i in range(position):
            node = node['next']
        return node

    def delete_pos(self, position):
        if position == 0:
            self.root = self.root['next']

        previous_node = self.get_node(position - 1)
        previous_node['next'] = previous_node['next']['next']

    def remove(self, node):
        if node == self.root:
            self.root = self.root['next']
            return

        previous_node = self.root
        while previous_node['next'] != node: # TODO: Add checks if element is not in list
            previous_node = previous_node['next']
        previous_node['next'] = previous_node['next']['next']

    def to_list(self):
        list_content = []
        next_element = self.root
        while next_element is not None:
            list_content.append(next_element['value'])
            next_element = next_element['next']
        return list_content


class DoubleLinkedList(LinkedList):
    def __init__(self):
        self.null_node = self._make_node(None, None, None)
        self.root = self.null_node

    def _make_node(self, element, previous_node, next_node):
        return {
            "value": element,
            "previous": previous_node,
            "next": next_node,
    }

    def insert(self, element):
        inserted = self._make_node(element, None, self.root)
        self.root['previous'] = inserted
        self.root = inserted

    def insert_in_pos(self, position, element):
        if position == 0:
            return self.insert(element)

        previous_node = self.get_node(position - 1)

        inserted_node = self._make_node(element, previous_node, previous_node['next']) 
        previous_node['next']['previous'] = inserted_node
        previous_node['next'] = inserted_node

    def remove(self, node):
        node['previous']['next'] = node['next']
        node['next']['previous'] = node['previous']

    def to_list(self):
        list_content = []
        next_element = self.root
        while next_element is not None and next_element is not self.null_node:
            list_content.append(next_element['value'])
            next_element = next_element['next']
        return list_content
