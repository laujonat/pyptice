"""
    <params> array, value
    array: [3,4,5,6,7,8]
    value: 7

    <output> int
    int: 4
    take pivot

    if pivot is equal to value
        return pivot
    if pivot > value
        array[pivot:-11]
        take next_pivot from array[pivot:-1]
    pivot < value
        array[0:pivot-1]
        take next_pivot from array[0: pivot-1]
"""


def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
