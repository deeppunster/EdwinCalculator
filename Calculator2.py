"""
Calculator2.py - another calculator program.
"""


def numbers(number_list):
    """
    Add up numbers in a list.
    :return: sum of the numbers
    """
    test_sum = 0
    for this_num in number_list:
        test_sum = test_sum + this_num
    return test_sum


if __name__ == '__main__':
    num_list = [1, 34, 3, 5, 9.0]
    sum_list = numbers(num_list)
    print(sum_list)
