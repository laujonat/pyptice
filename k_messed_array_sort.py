'''
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient 
function sortKMessedArray that sorts arr. 

For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array 
will be located at either index 4, 5, 6, 7 or 8 in the input array.
    
n = arr.length

# create an empty min-heap
h = new MinHeap()

# build the min-heap from the first k+1 elements of arr
h.buildHeap(arr[0,...,k])

for i from k+1 to n-1:
    # extract the top element from the min-heap and
    # assign it to the next available array index
    arr[i-(k+1)] = h.extractMin()

    # push the next array element into the min-heap
    h.insert(arr[i])

# extract all remaining elements from the min-heap
# and assign them to the next available array index
for i from 0 to k:
    arr[n-k-1 + i] = h.extractMin()
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
