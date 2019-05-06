'''
Given an unsorted array and a number n, find if there exists a pair of elements in the array whose difference is n.

Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
Output: Pair Found: (2, 80)

Input: arr[] = {90, 70, 20, 80, 50}, n = 45
Output: No Such Pair
'''


def find_pair(arr, target):
    sorted_list = sorted(arr)  # O(nlog(n))
    low = 0
    high = len(arr) - 1

    while low < high:
        difference = arr[high] - arr[low]
        if difference == target:
            return (arr[low], arr[high])
        elif target > difference:
            low += 1
        else:
            high -= 1


t1 = [5, 20, 3, 2, 50, 80]
n = 78
res = find_pair(t1, n)
print(res)

t2 = [90, 70, 20, 80, 50]
n = 45
res = find_pair(t2, n)
print(res)
