def find_pos_in_list(numbers, target_num):
    low_pos, high_pos = 0, len(numbers) - 1
    while low_pos < high_pos:
        middle = (high_pos + low_pos) // 2
        middle_num = numbers[middle]
        if middle_num > target_num:
            high_pos = middle - 1
        elif middle_num < target_num:
            low_pos = middle + 1
        else:
            return middle
    return low_pos


# pos = find_pos_in_list([2, 3, 4],3)
# print(pos)
