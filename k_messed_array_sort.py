'''
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient 
function sortKMessedArray that sorts arr. 

For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array 
will be located at either index 4, 5, 6, 7 or 8 in the input array.
'''
import heapq 

# O(n), O(n) space 
def sort_k_messed_array(arr, k):
  if k == 0:
    return arr

  minimum = 999
  for i in arr:
    if i < minimum:
      minimum = i

  result = []
  for i in range(0, len(arr)):
    result.append(minimum)
    minimum += 1

  return result
