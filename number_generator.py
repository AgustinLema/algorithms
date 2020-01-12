from numpy.random import randint


def generate_input_combinations(input_size, start_value=0, cap_value=5):
    if input_size <= 0:
        return [[]]

    combinations = []
    for num in range(start_value, cap_value):
        sub_combinations = generate_input_combinations(input_size-1,
                                                       start_value,
                                                       cap_value)
        for sub_sequence in sub_combinations:
            combinations.append([num] + sub_sequence)
    return combinations


def generate_random_inputs(input_size, input_count=10, value_count=10):
    def get_random(): return randint(0, value_count, input_size)
    generated_numbers = [list(get_random()) for i in range(input_count)]
    return generated_numbers


def generate_special_cases(input_size):
    ordered_asc = list(range(input_size))
    ordered_desc = list(range(input_size, 0, -1))
    all_same = [5] * input_size
    generated_numbers = [
        ordered_asc,
        ordered_desc,
        all_same
    ]
    return generated_numbers
