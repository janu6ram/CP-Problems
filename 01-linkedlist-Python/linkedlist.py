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
        # Your code goes here
        if self.head == None:
            self.head = new_element
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_element
        return

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        if position == 1:
            return self.head
        current = self.head
        count = 1
        while current.next != None:
            count += 1
            current = current.next
            # print(current.value, count)
            if count == position:
                return current
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here

        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return
        current = self.head
        count = 1
        while current.next != None:
            count += 1
            if count == position:
                new_element.next = current.next
                current.next = new_element
                return
            current = current.next
        if count + 1 == position:
            return current

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        if self.head == None:
            return
        if self.head.value == value:
            if self.head.next == None:
                self.head = None
                return
            self.head = self.head.next
            return
        current = self.head
        while current.next != None:
            if current.next.value == value:
                current = current.next
        return

    def printLList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
e4 = Element(4)
ll.insert(e4, 3)
ll.printLList()
print("pos of 3", ll.get_position(3).value)
ll.delete(1)
print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)
