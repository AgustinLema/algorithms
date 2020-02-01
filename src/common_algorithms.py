def partition(numbers, start, end):
    pivot_pos = end - 1
    pivot_value = numbers[pivot_pos]
    next_lower_index = start
    for pos in range(start, pivot_pos):
        number = numbers[pos]
        if number <= pivot_value:
            numbers[next_lower_index], numbers[pos] = numbers[pos], numbers[next_lower_index]
            next_lower_index += 1
    numbers[pivot_pos], numbers[next_lower_index] = numbers[next_lower_index], numbers[pivot_pos]
    return next_lower_index
