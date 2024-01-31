from question6 import selection_sort


def merge_lists_not_efficient(list_a: list, list_b: list) -> list:
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Expected arguments to be lists")
    # copy of list_a, with b appended
    extended_list = [value for value in list_a]
    extended_list.extend(list_b)
    selection_sort(extended_list)
    return extended_list
