import os
import logging
import array_algorithms
from number_generator import (
    generate_input_combinations,
    generate_special_cases,
    generate_random_inputs
)

from algorithm_benchmarker import export_benchmark_results, benchmark_algorithm_with_inputs

logging.basicConfig(level=logging.DEBUG)


def main():
    input_size = 300
    # inputs = generate_input_combinations(input_size, start_value=-input_size//2, cap_value=input_size//2)
    # inputs = [[1,4,2,4,5,5,2,1], [1, 1, 2, 3]]
    # inputs = generate_special_cases(800)

    inputs = generate_random_inputs(input_size, 4, input_size, -input_size)

    file_name = "array_algorithms_report.csv"
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass

    for algorithm in [
        array_algorithms.find_biggest_subarray_logn,
        array_algorithms.find_biggest_subarray_linear,
    ]:
        export_benchmark_results(benchmark_algorithm_with_inputs(algorithm, inputs, comparing_function=array_algorithms.find_biggest_subarray_linear), algorithm, file_name)

    file_name = "array_algorithms_report2.csv"
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass

    inputs = generate_random_inputs(input_size*250, 4, input_size, -input_size)
    k = 7
    def sort_and_find_index(x): return array_algorithms.sort_and_find_index(x, k)
    def center_partitioning_select(x): return array_algorithms.center_partitioning_select(x, k)

    for algorithm in [
        center_partitioning_select,
        sort_and_find_index
    ]:
        export_benchmark_results(benchmark_algorithm_with_inputs(algorithm, inputs, comparing_function=sort_and_find_index), algorithm, file_name)


if __name__ == "__main__":
    main()
