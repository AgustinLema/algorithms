import time
import logging
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


def main():
    input_size = 4
    inputs = generate_input_combinations(input_size, cap_value=input_size)
    # inputs = [[0, 0, 0, 0], [1, 1, 2, 3]]
    inputs = [[1,4,2,4,5,5,2,1], [1, 1, 2, 3]]

    #find_significant_input_data(sorting_algorithms.bubble_sort, inputs)

    #inputs = generate_random_inputs(50, 50)
    #find_significant_input_data(sorting_algorithms.bubble_sort, inputs)

    inputs = generate_special_cases(200)
    find_significant_input_data(sorting_algorithms.insertion_sort, inputs)
    logging.info("#" * 10)
    find_significant_input_data(sorting_algorithms.insertion_sort_with_binary_search, inputs)


if __name__ == "__main__":
    main()
