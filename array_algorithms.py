
def find_biggest_subarray_logn(numbers, start_pos=0, end_pos=None):
    if end_pos is None:
        end_pos = len(numbers)

    if start_pos + 1 == end_pos:
        # Single element list
        return numbers[start_pos]

    middle = (start_pos + end_pos-1) // 2
    left = find_biggest_subarray_logn(numbers, start_pos, middle + 1)
    right = find_biggest_subarray_logn(numbers, middle + 1, end_pos)
    cross = find_biggest_mid_subarray(numbers, start_pos, end_pos, middle)
    return max(left, right, cross)


def find_biggest_mid_subarray(numbers, start_pos, end_pos, middle):
    max_left, left_sum = 0, 0
    max_right, right_sum = 0, 0

    for i in range(middle - 1, start_pos - 1, -1):
        left_sum += numbers[i]
        if left_sum > max_left:
            max_left = left_sum

    for i in range(middle + 1, end_pos):
        right_sum += numbers[i]
        if right_sum > max_right:
            max_right = right_sum

    total = max_left + numbers[middle] + max_right
    return total


def find_biggest_subarray_linear(numbers):
    subarray_sum = 0
    subarray_max = 0
    for i in range(len(numbers)):
        subarray_sum += numbers[i]
        if subarray_sum < 0:
            subarray_sum = 0
        elif subarray_sum > subarray_max:
            subarray_max = subarray_sum
    return subarray_max


if __name__ == "__main__":
    result = find_biggest_subarray_logn([1, 2, 3, 4, -1])
    assert result == 10
    assert find_biggest_subarray_logn([9, -3, -2, 5, 2, -4, 3]) == 11
    result = find_biggest_subarray_linear([1, 2, 3, 4, -1])
    assert result == 10
    assert find_biggest_subarray_linear([9, -3, -2, 5, 2, -4, 3]) == 11