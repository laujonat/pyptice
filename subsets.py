'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
Set must not contain duplicate subsets.

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

# sorting O(nlog(n))
# call DFS
# for every element in list,


def subsets(nums):
    res = []
    dfs(sorted(nums), 0, [], res)
    return res


def dfs(nums, index, path, res):
    res.append(path)
    print("index", index)
    print("path", path)
    for i in range(index, len(nums)):
        dfs(nums, i + 1, path + [nums[i]], res)


t1 = [1, 2, 3]
res = subsets(t1)
print(res)
