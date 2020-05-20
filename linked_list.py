# Singly-Linked List - It contains a pointer to only the next node within the linked list.
# Double-Linked List - This is where there are pointers to both the next as well as the previous nodes.


class Node:
    """ A Node is a Singly-Linked List """
    def __init__(self, data_val=None, next_val=None):
        self.data_val = data_val
        self.next_val = next_val

    def __repr__(self):
        return repr(self.data_val)


# Custom Linked List
class LinkedList:
    def __init__(self):
        """ Creating a new Singly-Linked List """
        self.head = None

    def __repr__(self):
        """ Creating a string representation of the data in a list """
        nodes = []
        curr = self.head

        while curr:
            nodes.append(repr(curr))
            curr = curr.next_val

        return "[" + "->".join(nodes) + "]"

    def prepend(self, data_val):
        """ Insert a new element at the beginning of the list """
        self.head = Node(data_val=data_val, next_val=self.head)

    def append(self, data_val):
        """ Insert a new element at the end of list. """

        # Check if head is empty or not
        if not self.head:
            self.head = Node(data_val=data_val)
            return

        curr = self.head

        while curr.next_val:
            curr = curr.next_val

        curr.next_val = Node(data_val=data_val)

    def add_after(self, middle_data_val, data_val):
        """ Insert a new element after the node with middle_data_val """

        if middle_data_val is None:
            print("Data to insert after not specified")
            return

        curr = self.head

        while curr and curr.data_val != middle_data_val:
            curr = curr.next_val

        new_node = Node(data_val=data_val)
        new_node.next_val = curr.next_val
        curr.next_val = new_node

    def find(self, data):
        """ Search for the first element with data_val matching 'data'.
            Return the element or 'None' if not found. """

        curr = self.head
        while curr and curr.data_val != data:
            curr = curr.next_val

        return curr

    def remove(self, data):
        """ Remove the first occurence of 'data' in the list """

        curr = self.head
        prev = None

        while curr and curr.data_val != data:
            prev = curr
            curr = curr.next_val

        if prev is None:
            self.head = curr.next_val
        elif curr:
            prev.next_val = curr.next_val
            curr.next_val = None

    def reverse(self):
        """ Reverse the list in-place """

        curr = self.head

        prev_node = None
        next_node = None

        while curr:
            next_val = curr.next_val
            curr.next_val = prev_node

            prev_node = curr
            curr = next_val

        self.head = prev_node

    def reverse_recursive(self):
        """ Reverse the list in place using recursion """

        def recursion(curr, prev):
            if not curr:
                return prev

            next_val = curr.next_val
            curr.next_val = prev

            prev = curr
            curr = next_val

            return recursion(curr, prev)

        self.head = recursion(curr=self.head, prev=None)

    def count_nodes(self):
        """ Count the number of nodes in the linked list """

        if self.head is None:
            return 0
        else:
            curr = self.head
            count = 0
            while curr is not None:
                curr = curr.next_val
                count += 1
            return count


numbers = LinkedList()
print(f"Initial Level: {numbers}")

numbers.append("Two")
numbers.append("Three")
print(f"Append: {numbers}")

numbers.prepend("One")
print(f"Prepend: {numbers}")

numbers.append("Four")
numbers.append("Five")
numbers.append("Seven")
print(f"Append: {numbers}")

numbers.add_after("Five", "Six")
print(f"Add After: {numbers}")

numbers.reverse()
print(f"Reverse: {numbers}")

numbers.reverse_recursive()
print(f"Reverse Recursive: {numbers}")

numbers.remove("One")
print(f"Remove: {numbers}")

numbers.remove("Six")
print(f"Remove: {numbers}")

print(f"Count Nodes: {numbers.count_nodes()}")