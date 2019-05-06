from typing import List


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
