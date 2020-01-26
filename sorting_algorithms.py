from searching_algorithms import find_pos_in_list
from data_structures import MaxHeap


def bubble_sort(numbers):
    numbers_len = len(numbers)
    for starting_pos in range(numbers_len - 1):
        for left_compared_pos in range(numbers_len - 1 - starting_pos):
            if (numbers[left_compared_pos] > numbers[left_compared_pos + 1]):
                right_pos = left_compared_pos + 1
                numbers[left_compared_pos], numbers[right_pos] = numbers[right_pos], numbers[left_compared_pos]
    return numbers


def bubble_sort_memory(numbers):
    numbers_len = len(numbers)
    last_flipped = numbers_len - 1

    for starting_pos in range(numbers_len - 1):
        end_pos = numbers_len - 1 - starting_pos
        if last_flipped > end_pos:
            # I didn't flip anything, the list is already ordered
            break
        elif last_flipped < end_pos:
            end_pos = last_flipped

        for curr_pos in range(end_pos):
            next_pos = curr_pos + 1
            if (numbers[curr_pos] > numbers[next_pos]):
                numbers[curr_pos], numbers[next_pos] = numbers[next_pos], numbers[curr_pos]
                last_flipped = curr_pos

    return numbers


def insertion_sort(numbers):
    #  Read from left to right starting from second one.
    #  pick the number and compare it with the ones on its left
    #  If the number is bigger, stop
    #  If the number is smaller, move smaller to right.
    numbers_len = len(numbers)
    for picked_pos in range(1, numbers_len):
        picked_num = numbers[picked_pos]
        for comp_pos in range(picked_pos - 1, -1, -1):
            comp_num = numbers[comp_pos]
            if comp_num <= picked_num:
                break
            else:
                numbers[comp_pos + 1] = comp_num
                numbers[comp_pos] = picked_num
    return numbers


def insertion_sort_flip_by_shift(numbers):
    #  Has worse performance than default insertion sort.
    #  The difference is that it doesn't flip numbers right away
    #  This one calculates the shift first before moving
    #  This will be useful for the version with binary search
    numbers_len = len(numbers)
    for picked_pos in range(1, numbers_len):
        picked_num = numbers[picked_pos]
        shift = 0

        # Find required shift
        for comp_pos in range(picked_pos - 1, -1, -1):
            comp_num = numbers[comp_pos]
            if comp_num <= picked_num:
                break
            else:
                shift += 1

        # Make the shift
        for comp_pos in range(picked_pos - 1, picked_pos - shift - 1, -1):
            numbers[comp_pos + 1] = numbers[comp_pos]
        numbers[picked_pos - shift] = picked_num

    return numbers


def insertion_sort_with_binary_search(numbers):
    numbers_len = len(numbers)
    for picked_pos in range(1, numbers_len):
        picked_num = numbers[picked_pos]

        if picked_num >= numbers[picked_pos - 1]:
            # Already bigger, skip to next
            continue

        shift = 0

        # Find required shift using binary search
        desired_position = find_pos_in_list(numbers[0:picked_pos], picked_num)
        shift = picked_pos - desired_position

        # Make the shift
        for comp_pos in range(picked_pos - 1, picked_pos - shift - 1, -1):
            numbers[comp_pos + 1] = numbers[comp_pos]
        numbers[picked_pos - shift] = picked_num

    return numbers


def selection_sort(numbers):
    # Find smallest element in list and move to pos 0
    # Find smallest element in rest of list and move to pos 1
    # Etc
    numbers_len = len(numbers)
    for pos_to_fill in range(0, numbers_len - 1):
        min_value_pos = pos_to_fill
        for pos_pointer in range(pos_to_fill + 1, numbers_len):
            if numbers[pos_pointer] < numbers[min_value_pos]:
                min_value_pos = pos_pointer

        numbers[pos_to_fill], numbers[min_value_pos] = numbers[min_value_pos], numbers[pos_to_fill]
    return numbers


def merge_sort(numbers, start_pos=None, end_pos=None):
    # Divide and conquer: take first half and sort it, same with second half, then mix them.
    # The middle is included in the first half

    if (start_pos is None):
        start_pos = 0
    if (end_pos is None):
        end_pos = len(numbers) - 1

    # Exit condition. If list is just one element, then return it.
    if start_pos == end_pos:
        return numbers

    middle = (start_pos + end_pos) // 2
    assert middle != -1
    merge_sort(numbers, start_pos, middle), merge_sort(numbers, middle + 1, end_pos)

    l_pointer, r_pointer = start_pos, middle + 1
    ordered = []
    for new_pos in range(start_pos, end_pos + 1):
        if r_pointer > end_pos or (l_pointer <= middle and numbers[l_pointer] <= numbers[r_pointer]):
            ordered.append(numbers[l_pointer])
            l_pointer += 1
        else:
            ordered.append(numbers[r_pointer])
            r_pointer += 1
    numbers[start_pos:end_pos + 1] = ordered[:]
    return numbers


def heap_sort_extracting(numbers):
    mh = MaxHeap(numbers)
    return [mh.extract_max() for i in range(len(mh.elements))][::-1]


def heap_sort_in_place(numbers):
    mh = MaxHeap(numbers)
    mh.get_sorted_list()
    return numbers


def quick_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if start >= end:
        return
    pivot_pos = qs_partition(numbers, start, end)
    quick_sort(numbers, start, pivot_pos)
    quick_sort(numbers, pivot_pos + 1, end)
    return numbers


def quick_sort_center_pivot(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if start >= end:
        return
    middle = (start + end) // 2
    numbers[middle], numbers[end - 1] = numbers[end - 1], numbers[middle]
    pivot_pos = qs_partition(numbers, start, end)
    quick_sort_center_pivot(numbers, start, pivot_pos)
    quick_sort_center_pivot(numbers, pivot_pos + 1, end)
    return numbers


def qs_partition(numbers, start, end):
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


def counting_sort(numbers, k=1000, getf=lambda n: n):
    counts = [0] * k
    numbers_len = len(numbers)
    ordered = [0] * numbers_len
    # Count how many occurences of each number
    for i in range(numbers_len):
        number = getf(numbers[i])
        counts[number] += 1
    # Add the count of previous numbers so that we store total amount of numbers equal or smaller for each pos
    for i in range(1, k):
        counts[i] += counts[i-1]

    for i in range(numbers_len - 1, -1, -1):
        number = numbers[i]
        pos = counts[getf(number)]
        ordered[pos - 1] = number
        counts[getf(number)] -= 1
    return ordered


def radix_sort(numbers, base=10):
    max_number = max(numbers) 
    num_digits = 1
    while max_number > 10:
        num_digits += 1
        max_number //= 10

    for digit in range(num_digits):
        numbers = counting_sort(numbers, base, lambda n: (n // base**digit) % base)
    return numbers


builtin_sort = sorted

if __name__ == "__main__":
    print("selection sort: ", merge_sort([1,5,2,3215,2365,346,23,121,5,56,3]))
    print("heap_sort_extracting sort: ", heap_sort_extracting([1,5,2,3215,2365,346,23,121,5,56,3]))
    print("quick_sort: ", quick_sort([1,5,2,3215,2365,346,23,121,5,56,3]))
    print("quick_sort center pivot: ", quick_sort_center_pivot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
    print("counting sort ", counting_sort([1,5,2,3215,2365,346,23,121,5,56,3], 3216))
    print("radix sort ", radix_sort([1,5,2,3215,2365,346,23,121,5,56,3]))
