from searching_algorithms import find_pos_in_list


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


builtin_sort = sorted

#print("Insertion sort: ", insertion_sort_with_binary_search([1,5,2,3215,2365,346,23,121,5,56,3]))
