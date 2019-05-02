from bisect import bisect_left
'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
'''
    nums = 10, 15, 3, 7
    sorted = 3, 7 10, 15
    low, high = 0, 3
    p1. rsum = 3 + 15 = 18
    p2. rsum = 7 + 15 = 22
    p3. rsum = 10 + 15 = 25
'''


def two_sum(lst, K):
    lst.sort()
    # O(n)
    for i in range(len(lst)):
        target = K - lst[i]
        j = binary_search(lst, target)  # O(log(n))

        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False


def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1


test = [10, 15, 3, 7]
print(check_sum(test, 17))
