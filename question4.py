# Entry Point
def main():
    num_stars_input = input('Please enter a positive even number for starting amount of stars: ')
    while not num_stars_input.isnumeric() or int(num_stars_input) % 2 != 0:
        num_stars_input = input("Invalid Input! input must be a positive even number. please try again: ")

    num_stars = int(num_stars_input)
    del num_stars_input
    print_star_pattern(num_stars)


def print_star_pattern(num_stars: int):
    """
    prints out a pattern of stars(*) and @ sign using the following the pattern: num_stars, num_stars-2, num_stars-4 ... 2
    :param num_stars: num of stars to be printed
    :return:
    """
    # start with a given value and decrement by 2 each time until we reach 0
    for star_times in range(num_stars, 0, -2):
        print(('*' * star_times) + '@', end='')
    print()


if __name__ == '__main__':
    main()
