"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        count = 1
        result = None
        current = self.head
        if self.head:
            while current:
                if position == count:
                    result = current
                    break
                count += 1
                current = current.next
        return result

    def insert(self, new_element, position):
        counter = 1
        if position == 1:
            next_element.next = self.head
            self.head = new_element
        else:
            current = self.head
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        prev = self.head
        current = self.head.next
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
                return self.head
            while current:
                if value == current.value:
                    prev.next = current.next.next
                    if prev:
                        prev.next = current.next
                prev = current
                current = current.next

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if not self.head:
            return None
        res = self.head
        copy = res.next
        self.head = copy
        return res


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# print(ll.head.next.next.value)
# Should also print 3
print("get_position(3)", ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print("after insert (e4, 3)", ll.get_position(3).value)

# Test delete
ll.delete(2)
# Should print 2 now
print("delete pos 2, print 1", ll.get_position(1).value)
# Should print 4 now
print("pos 2, print 4", ll.get_position(2).value)
# Should print 3 now
print("pos 3, print 3", ll.get_position(3).value)

# With Stack
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
