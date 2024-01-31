def main():
    candidate = input('Please enter a string to be evaluated as palindrome: ')
    print(f"{candidate} is {'' if is_palindrome(candidate) else 'not '}a palindrome")


def is_palindrome(candidate: str, left_index: int=0, right_index: int=-1) -> bool:
    """
    Gets a string and checks if it is a palindrome
    :param candidate: a string to be checked
    :param left_index: the index of the left char to compare
    :param right_index: the index of the right index to compare. -1 is used to indicate the right-most character
    :return:
    """

    # checks if we given the default value for right index. if it was given, set the right index to the last element
    if right_index == -1:
        right_index = len(candidate) -1

    # an empty string is a palindrome by definition
    if candidate == '':
        return True

    # base condition. if we reached the middle values and they are equal, return true
    if left_index == right_index:
        return True
    if left_index == right_index - 1:
        return candidate[left_index] == candidate[right_index]

    # step. recursively call is palindrome on candidate while moving the indices toward the middle
    return (candidate[right_index] == candidate[left_index]) and is_palindrome(candidate, left_index + 1, right_index - 1)


if __name__ == '__main__':
    main()
