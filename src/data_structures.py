import math


class MaxHeap:
    def __init__(self, elements):
        self.elements = elements
        self._left = lambda i: (i + 1) * 2 - 1
        self._right = lambda i: (i + 1) * 2
        self._parent = lambda i: (i + 1) // 2 - 1
        self.heap_len = len(elements)
        self.rebuild_max_heap()

    def rebuild_max_heap(self):
        last_idx = self.heap_len - 1
        last_parent = self._parent(last_idx)
        for i in range(last_parent, -1, -1):
            self.heapify(i)

    def heapify(self, index):
        highest_value = self.elements[index]

        indexes = [i  for i in [self._left(index), self._right(index)] if self.heap_len > i]
        swap_idx = index

        for position in indexes:
            if self.elements[position] > highest_value:
                swap_idx = position
                highest_value = self.elements[position]

        if swap_idx != index:
            self.elements[index], self.elements[swap_idx] = \
                self.elements[swap_idx], self.elements[index]
            self.heapify(swap_idx)

    def get_sorted_list(self):
        while self.heap_len > 0:
            self.heapify(0)
            highest = self.elements[0]
            last = self.elements[self.heap_len - 1]
            self.elements[self.heap_len - 1], self.elements[0] = highest, last
            self.heap_len -= 1
        return self.elements

    def maximum(self):
        return self.elements[0]

    def extract_max(self):
        self.heap_len -= 1
        if len(self.elements) == 1:
            return self.elements.pop(0)

        max_value = self.elements[0]
        self.elements[0] = self.elements.pop()
        self.heapify(0)
        return max_value

    def increase_key(self):
        pass

    def insert_key(self):
        pass

    def draw_tree(self):
        numbers_per_level = 1
        elements_len = len(self.elements)
        sub_levels = int(math.log(elements_len))
        idx = 0
        while idx < elements_len:
            line = [" " * sub_levels]
            for n in range(numbers_per_level):
                number = self.elements[idx]
                line.append(str(number))
                idx += 1
                if idx >= len(self.elements):
                    break
            print(" ".join(line))
            sub_levels -= 1
            numbers_per_level *= 2


if __name__ == "__main__":
    elements = [5, 2, 51, 9, 3, 2, 55, 7, 1, 3]
    heap_elements = elements[:]
    mh = MaxHeap(heap_elements)
    print(mh.maximum(), "should be biggest value")
    assert mh.maximum() == 55
    ordered = mh.get_sorted_list()
    print(ordered)
    assert ordered == sorted(elements)
