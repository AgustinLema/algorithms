import time
import logging
import os
from number_generator import (generate_input_combinations,
                              generate_random_inputs,
                              generate_special_cases)
from benchmark_analysis import print_analysis
import sorting_algorithms

logging.basicConfig(level=logging.DEBUG)

MIN_RUN_TIME = 0


def benchmark_algorithm(algorithm, input, times_sampling=20):
    run_times = [get_algorithm_run_time(algorithm, input)
                 for i in range(times_sampling)]

    return min(run_times)


def get_algorithm_run_time(algorithm, input, run_count=1):
    start = time.time()
    for i in range(run_count):
        result = algorithm(input[:])

    run_time = time.time() - start
    assert result == sorted(input)

    if run_time <= MIN_RUN_TIME:
        run_time = get_algorithm_run_time(algorithm, input, run_count*10)
    else:
        # TODO: Use median instead of average, there can be peaks
        run_time /= run_count

    return run_time


def find_significant_input_data(algorithm, inputs):
    results = {}

    for input in inputs:
        time = benchmark_algorithm(algorithm, input)
        results[str(input)] = time

    print_analysis(results)


def export_algorithm_benchmark(algorithm, inputs, file_name):
    with open(file_name, 'a') as f:
        for input in inputs:
            time = benchmark_algorithm(algorithm, input)
            f.write(";".join([
                algorithm.__name__,
                str(input),
                str(time)]))
            f.write("\n")


def main():
    input_size = 4
    inputs = generate_input_combinations(input_size, cap_value=input_size)
    # inputs = [[0, 0, 0, 0], [1, 1, 2, 3]]
    inputs = [[1,4,2,4,5,5,2,1], [1, 1, 2, 3]]

    #find_significant_input_data(sorting_algorithms.bubble_sort, inputs)

    #inputs = generate_random_inputs(50, 50)
    #find_significant_input_data(sorting_algorithms.bubble_sort, inputs)

    inputs = generate_special_cases(800)
    #find_significant_input_data(sorting_algorithms.insertion_sort, inputs)
    #logging.info("#" * 10)

    file_name = "exported.csv"
    os.remove(file_name)

    for algorithm in [
        sorting_algorithms.bubble_sort,
        sorting_algorithms.bubble_sort_memory,
        sorting_algorithms.insertion_sort,
        sorting_algorithms.insertion_sort_flip_by_shift,
        sorting_algorithms.insertion_sort_with_binary_search,
        sorting_algorithms.builtin_sort,
        sorting_algorithms.selection_sort,
        sorting_algorithms.merge_sort
    ]:
        export_algorithm_benchmark(algorithm, inputs, file_name)


if __name__ == "__main__":
    main()
