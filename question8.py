# wrapping all list as a queue like structure
class _ListQueueIterator:
    """Wrap lists like a walkable queue for easier linear access"""
    def __init__(self, to_walk: list):
        self._to_walk = to_walk
        self._to_walk_length = len(to_walk)
        self._current_index = 0

    def is_at_end(self) -> bool:
        """Check if last value was polled"""
        return self._current_index == self._to_walk_length

    def peek(self):
        """take current value but don't move forward, return None at end"""
        if self._current_index < self._to_walk_length:
            return self._to_walk[self._current_index]
        else:
            return None

    def poll(self):
        """return current value and move forward"""
        if self._current_index < self._to_walk_length:
            return_value = self.peek()
            self._current_index += 1
            return return_value
        else:
            return None


def merge_efficient(list_a, list_b) -> list:
    """
    Take in to lists and merges them together
    :param list_a: first list to be merged must be sortd
    :param list_b: second list to be merged must be sorted
    :return: new list made of the given lists in
    """
    if not isinstance(list_a, list):
        raise TypeError('Expected list_a to be of type\'list\'')
    if not isinstance(list_b, list):
        raise TypeError('Expected list_b to be of type\'list\'')
    list_a_iterator = _ListQueueIterator(list_a)
    list_b_iterator = _ListQueueIterator(list_b)
    merged_list = []

    # appending values from list_a and list_b until reaches the end of one of them
    while (not list_a_iterator.is_at_end()) and (not list_b_iterator.is_at_end()):
        # current value in list_a is smaller
        if list_a_iterator.peek() < list_b_iterator.peek():
            merged_list.append(list_a_iterator.poll())
        # current value in list_b is smaller
        elif list_b_iterator.peek() < list_a_iterator.peek():
            merged_list.append(list_b_iterator.poll())
        # values are equal
        else:
            merged_list.append(list_a_iterator.poll())
            merged_list.append(list_b_iterator.poll())

    # append remaining items of list_a
    while not list_a_iterator.is_at_end():
        merged_list.append(list_a_iterator.poll())

    # append remaining items of list_b
    while not list_b_iterator.is_at_end():
        merged_list.append(list_b_iterator.poll())

    return merged_list
