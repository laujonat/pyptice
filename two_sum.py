from typing import List


# def twoSum(nums: List[int], target: int) -> List[int]:
# if len(nums) == 0:
# return False
# sorted_list = sorted(nums)
# min_idx = 0
# max_idx = len(nums) - 1

# for _ in range(len(sorted_list)):
# _sum = sorted_list[min_idx] + sorted_list[max_idx]
# if _sum == target:
# v1, v2 = sorted_list[min_idx], sorted_list[max_idx]
# return [nums.index(v1), nums.index(v2)] # fail case: [3, 3]
# elif _sum < target:
# min_idx += 1
# else:
# max_idx -= 1

def twoSum(self, nums: List[int], target: int) -> List[int]:
    checked = {}
    for i, e in enumerate(nums):
        compliment = target - e
        if compliment in checked:
            return [checked[compliment], i]
        checked[e] = i
    return []


twoSum(nums=[1, 3, 4], target=7)
twoSum(nums=[3, 2, 4], target=6)
