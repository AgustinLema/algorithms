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


def generate_inputs(input_size, input_count=10, value_count=100):
    generated_numbers = [12345, 54321]
    generated_numbers = [randint(0, value_count, input_size) for i in range(input_count)]
    return generated_numbers


def benchmark_algorithm(algorithm, input, run_count=1):
    start = time.time()
    for i in range(run_count):
        result = algorithm(input)

    run_time = time.time() - start
    assert result == sorted(input)

    if run_time < MIN_RUN_TIME:
        run_time = benchmark_algorithm(algorithm, input, run_count*10)
    else:
        run_time /= run_count

    return run_time


def find_significant_input_data(algorithm, input_size, input_count):
    results = {}
    inputs = generate_inputs(input_size, input_count)
    for input in inputs:
        time = benchmark_algorithm(algorithm, input)
        results[str(input)] = time

    for input, time in results.items():
        logging.info(f"{input}, {time}")

    slowest = max(results, key=results.get)
    average = median(results, key=results.get)
    fastest = min(results, key=results.get)

    for key in slowest, average, fastest:
        print(f"{key}, {results[key]}")


def main():
    input_size = 10
    input_count = 1000
    find_significant_input_data(sorting_algorithms.builtin_sort, input_size, input_count)


if __name__ == "__main__":
    main()
