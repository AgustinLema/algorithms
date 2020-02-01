import os, sys
sys.path.insert(0, "src")

import sorting_algorithms

def test_algorithms():
    numbers = [1, 5, 2, 715, 965, 346, 23, 121, 5, 56, 3]
    sorted_numbers = sorted(numbers)
    algorithms = [
            sorting_algorithms.bubble_sort,
            sorting_algorithms.bubble_sort_memory,
            sorting_algorithms.insertion_sort,
            sorting_algorithms.insertion_sort_flip_by_shift,
            sorting_algorithms.insertion_sort_with_binary_search,
            sorting_algorithms.builtin_sort,
            sorting_algorithms.selection_sort,
            sorting_algorithms.merge_sort,
            sorting_algorithms.heap_sort_extracting,
            sorting_algorithms.heap_sort_in_place,
            sorting_algorithms.quick_sort,
            sorting_algorithms.quick_sort_center_pivot,
            sorting_algorithms.counting_sort,
            sorting_algorithms.radix_sort,
        ]
    for algorithm in algorithms: 
        assert sorted_numbers == algorithm(numbers[:])
