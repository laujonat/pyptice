# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Approach
Find the middle of the linked list.
L = LinkedNodes
P = LinkedNodes // 2
By definition:
    Node(p) => All nodes to the left are <= Node(p)
    Node(p) => All nodes to the right are >= Node(p)

1 -> 2 -> 3 -> 4 -> 5 -> None

Approach
1) Find P
    - Use slow and fast pointer. When fast pointer reaches None, slow pointer is at mid point
2) Separate left and right sides of L
    - Start of left can be the head
    - Use a pointer to track where the midpoint will be for the right side
3) Recursively call left the right

Edge case
1) When length of L is 1
"""


def sortedListToBST(self, head: ListNode) -> TreeNode:
    if not head:
        return None

    prev = None
    slow = head
    fast = head

    while fast and fast.next:
        prev = slow  # Start of right side
        slow = slow.next
        fast = fast.next.next

    # Disconnect left side
    if prev:
        prev.next = None

    pivot = prev
    mid_root = TreeNode(pivot.val)

    # One element in the list
    if head == pivot:
        return mid_root

    # Form the tree
    mid_root.left = self.sortedListToBST(head)
    mid_root.right = self.sortedListToBST(pivot.next)
    return mid_root
