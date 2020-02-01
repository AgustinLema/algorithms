import time
import os

MIN_RUN_TIME = 0


def get_algorithm_run_time(algorithm, input, run_count=1, comparing_function=None):
    start = time.time()
    for i in range(run_count):
        result = algorithm(input[:])

    run_time = time.time() - start
    if comparing_function is not None:
        assert result == comparing_function(input), "Algorithm %s output is returning %s when expected output is %s" % (algorithm.__name__, result, comparing_function(input))

    if run_time <= MIN_RUN_TIME:
        run_time = get_algorithm_run_time(algorithm, input, run_count*10)
    else:
        # TODO: Use median instead of average, there can be peaks
        run_time /= run_count

    return run_time


def benchmark_algorithm(algorithm, input, times_sampling=20, comparing_function=None):
    run_times = [get_algorithm_run_time(algorithm, input, comparing_function=comparing_function)
                 for i in range(times_sampling)]

    return min(run_times)


def benchmark_algorithm_with_inputs(algorithm, inputs, times_sampling=20, comparing_function=None):
    results = {}

    for input in inputs:
        time = benchmark_algorithm(algorithm, input, times_sampling, comparing_function)
        results[str(input)] = time

    return results


def export_benchmark_results(results, algorithm, file_name):
    with open(file_name, 'a') as f:
        for input, run_time in results.items():
            f.write(";".join([
                algorithm.__name__,
                str(input),
                str(run_time)]))
            f.write("\n")
