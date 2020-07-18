class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        self.insert(self.root, new_val)

    def insert(self, start, new_value):
        if start == None:
            start.value = new_value
            return
        if start.value < new_value:
            insert(start.right, new_value)
        else:
            insert(start.left, new_value)

    def printSelf(self):
        # Your code goes here
        printSelf(self.root)

    def printSelf(self, start):
        if start == None:
            return
        self.printSelf(start.left)
        print(start.value),
        self.printSelf(start.right)

    def search(self, find_val):
        # Your code goes here
        return self.search_new(self.root, find_val)

    def search_new(self, start, find_val):
        if start == None or type(start.value) != type(find_val):
            return False
        if start.value == find_val:
            return True
        if start.value < find_val:
            return self.search_new(start.right, find_val)
        else:
            return self.search_new(start.left, find_val)
