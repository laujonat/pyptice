'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

O(n) solution exits with O(1) space.
'''

# S = lst[i] + lst[j], such that j != i + 1 and j != i - 1
'''
0: [2, 5]
1: [2, 6, 5]
2: [4, 2]
3: [4, 5]
'''


def largest_adj_sum(lst):
    incl = 0
    excl = 0
    new_excl = 0
    i = 0
    while i < len(lst):
        new_excl = excl if excl > incl else incl

        incl = excl + lst[i]
        excl = new_excl
        i += 1
    return max(incl, excl)


# return 13
t1 = [2, 4, 6, 2, 5]
t2 = [5, 1, 1, 5]
res = largest_adj_sum(t2)
print(res)
