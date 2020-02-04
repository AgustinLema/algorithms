class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, element):
        parent = None
        possible_position = self.root
        while possible_position is not None:
            parent = possible_position
            if element <= possible_position['value']:
                possible_position = possible_position['left-child']
            else:
                possible_position = possible_position['right-child']

        node = {
                'value': element,
                'parent': parent,
                'left-child': None,
                'right-child': None,
        }
        if parent is None:
            self.root = node
        else:
            node = {
                'value': element,
                'parent': parent,
                'left-child': None,
                'right-child': None,
            }
            if element <= parent['value']:
                parent['left-child'] = node
            else:
                parent['right-child'] = node

    def insert_list(self, elements):
        for element in elements:
            self.insert(element)

    def search(self, element):
        node = self.root
        while node is not None and node['value'] != element:
            if element <= node['value']:
                node = node['left-child']
            else:
                node = node['right-child']
        return node

    def minimum(self, node=None):
        if node is None:
            node = self.root
        while node['left-child'] is not None:
            node = node['left-child']
        return node

    def maximum(self, node=None):
        if node is None:
            node = self.root
        while node['right-child'] is not None:
            node = node['right-child']
        return node

    def predecessor(self, node):
        if node['left-child'] is not None:
            return self.maximum(node)
        else:
            while node['parent'] is not None and node['parent']['right-child'] != node:
                node = node['parent']
            return node['parent']

    def successor(self, node):
        if node['right-child'] is not None:
            return self.minimum(node)
        else:
            while node['parent'] is not None and node['parent']['left-child'] != node:
                node = node['parent']
            return node['parent']

    def get_sorted_list(self, node=None):
        if node is None:
            if self.root is None:
                return
            node = self.root
        sorted_list = []
        if node['left-child'] is not None:
            sorted_list += self.get_sorted_list(node['left-child'])
        sorted_list.append(node['value'])
        if node['right-child'] is not None:
            sorted_list += self.get_sorted_list(node['right-child'])
        return sorted_list

    def transplant(self, element):
        pass
    
    def remove(self, element):
        pass
