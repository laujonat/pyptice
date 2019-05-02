'''
Given an array containing n+1 integers where each integer is between 1 and n (inclusive)
Prove at least one duplicate number exists
'''


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)


solution = Solution()
dup = solution.findDuplicate([1, 2, 3, 3, 4, 5])
print(dup)
