"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Approach
1) Select a pivot at the middle of the array
2) Do the same for the left and right sides of the array
"""
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None



def sorted_bst(nums: List(int)): -> int
  if not nums:
    return None
  
  pivot = len(nums) // 2
  root = TreeNode(nums[pivot])
  root.left = sorted_bst(nums[:pivot])
  root.right = soted_bst(nums[pivot+1:])
  return root
