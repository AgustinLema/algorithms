import asyncio
from random import randint

def algorithm(text):
    return sorted(text)


import time

def benchmark(func, *args):
    run_count=0
    start_time=time.time()
    end_time=start_time + 1
    curr_time=start_time

    while curr_time < end_time:
        func(*args)
        run_count+=1
        curr_time = time.time()
    total_time = curr_time-start_time
    print(total_time, run_count)
    return total_time/run_count

numbers= [ randint(0, 1000000) for i in range(5000000) ]
print("Numbers generated")
print(benchmark(algorithm, numbers ))