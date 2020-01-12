import time
import logging
from numpy.random import randint
from statistics import median as median_statistics
import sorting_algorithms

logging.basicConfig(level=logging.DEBUG)

MIN_RUN_TIME = 0.001


def median(*iterable, key):
    median_statistics
    return max(*iterable, key=key)


def generate_input_combinations(input_size, start_value=0, cap_value=5):
    if input_size <= 0:
        return [[]]

    combinations = []
    for num in range(start_value, cap_value):
        sub_combinations = generate_input_combinations(input_size-1, start_value, cap_value)
        for sub_sequence in sub_combinations:
            combinations.append([num] + sub_sequence)
    return combinations


def generate_random_inputs(input_size, input_count=10, value_count=10):
    generated_numbers = [list(randint(0, value_count, input_size)) for i in range(input_count)]
    return generated_numbers


def benchmark_algorithm(algorithm, input, run_count=80000):
    start = time.time()
    for i in range(run_count):
        result = algorithm(input)

    run_time = time.time() - start
    assert result == sorted(input)

    if run_time < MIN_RUN_TIME:
        run_time = benchmark_algorithm(algorithm, input, run_count*10)
    else:
        run_time /= run_count  # TODO: Use median instead of average, there can be peaks

    return run_time


def find_significant_input_data(algorithm, input_size, input_count):
    results = {}
    # inputs = generate_random_inputs(input_size, input_count)
    inputs = generate_input_combinations(input_size, cap_value=input_size)
    print(inputs)
    for input in inputs:
        time = benchmark_algorithm(algorithm, input)
        results[str(input)] = time

    for input, time in results.items():
        if "1, 1, 1," in input or True:
            logging.info(f"{input}, {time}")

    slowest = max(results, key=results.get)
    average = median(results, key=results.get)
    fastest = min(results, key=results.get)

    logging.info("Important data")
    for key in slowest, average, fastest:
        logging.info(f"{key}, {results[key]}")


def main():
    input_size = 3
    input_count = 1000
    find_significant_input_data(sorting_algorithms.builtin_sort, input_size, input_count)


if __name__ == "__main__":
    main()
