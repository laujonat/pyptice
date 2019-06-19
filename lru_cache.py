'''
Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n, and
contain the following methods:

set(key, value): sets key to value.
If there are already n items in the cache and we are adding a new item,
then it should also remove the least recently used item.

get(key): gets the value at key. If no such key exists, return null.

'''


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None, 0)
        self.tail = Node(None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev

    '''
    Tail must always point to the last node insert
    Set tail to previous node
    Set next pointer to node
    Set prev to the new previous node
    Set next as tail
    Set the new tail prev to node
    '''

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


class LRUCache:
    def __init__(self, n):
        self.n = n
        self.dict = {}
        self.list = LinkedList()

    def set(self, key, val):
        if key in self.dict:
            self.dict[key].delete()
        n = Node(key, val)
        self.list.add(n)
        self.dict[key] = n
        if len(self.dict) > self.n:
            head = self.list.get_head()
            self.list.remove(head)
            del self.dict[head.key]

    def get(self, key):
        if key in self.dict:  # Still O(1)
            n = self.dict[key]
            self.list.remove(n)
            self.list.add(n)
            return n.val
