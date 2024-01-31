def find_minimum_index(to_check: list, start_index: int) -> int:
    minimum_index = start_index
    length_of_list = len(to_check)
    for index in range(minimum_index + 1, length_of_list):
        if to_check[index] < to_check[minimum_index]:
            minimum_index = index
    return minimum_index


def selection_sort(to_sort: list):
    # Check type of argument
    if not isinstance(to_sort, list):
        raise TypeError('Expected to_sort to be of type\'list\'')
    length_of_list = len(to_sort)
    for current_index in range(length_of_list):
        # find minimum
        minimum_index = find_minimum_index(to_sort, current_index)
        # swap, nicer way to write it in python
        if minimum_index != current_index:
            to_sort[current_index], to_sort[minimum_index] = to_sort[minimum_index], to_sort[current_index]

