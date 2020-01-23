import time
import logging
import os
from number_generator import (generate_input_combinations,
                              generate_random_inputs,
                              generate_special_cases)
from algorithm_benchmarker import export_benchmark_results, benchmark_algorithm_with_inputs
import sorting_algorithms

logging.basicConfig(level=logging.DEBUG)


def main():
    input_size = 4
    inputs = generate_input_combinations(input_size, cap_value=input_size)
    # inputs = [[0, 0, 0, 0], [1, 1, 2, 3]]
    inputs = [[1,4,2,4,5,5,2,1], [1, 1, 2, 3]]

    #find_significant_input_data(sorting_algorithms.bubble_sort, inputs)

    #inputs = generate_random_inputs(800, 10,800)
    #print(benchmark_algorithm_with_inputs(sorting_algorithms.quick_sort, inputs, comparing_function=sorted))
    #find_significant_input_data(sorting_algorithms.bubble_sort, inputs)

    inputs = generate_special_cases(800)
    #find_significant_input_data(sorting_algorithms.insertion_sort, inputs)
    #logging.info("#" * 10)

    file_name = "sorting_algorithms_report.csv"
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass

    for algorithm in [
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
    ]:
        export_benchmark_results(benchmark_algorithm_with_inputs(algorithm, inputs, comparing_function=sorted), algorithm, file_name)


if __name__ == "__main__":
    main()
