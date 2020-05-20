# Head - Root
# Path - Edges
# Last Node - Leaf
# Complexity is O(n)
# Worst Case - Complexity is O(n)
from queue_module import MyQueue


class Node:
    def __init__(self, data):
        self.__left = None
        self.__right = None
        self.__data = data

    def get_left_child(self):
        return self.__left

    def set_left_child(self, left):
        self.__left = left

    def get_right_child(self):
        return self.__right

    def set_right_child(self, right):
        self.__right = right

    def get_value(self):
        return self.__data

    def set_value(self, value):
        self.__data  = value

    def print_tree(self):
        if self.__left:
            self.__left.print_tree()

        print(self.__data)

        if self.__right:
            self.__right.print_tree()


def insert(head, node):
    if head is None:
        return node

    if node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), node))
    else:
        head.set_right_child(insert(head.get_right_child(), node))

    return head


def lookup(head, data):
    if head is None:
        return print("Value not found")

    if head.get_value() == data:
        return head

    if data < head.get_value():
        return lookup(head.get_left_child(), data)
    else:
        return lookup(head.get_right_child(), data)


def print_node(node):
    if node is None:
        print("Not Found")

    print(node.get_value())


def min_value(head):
    curr = head

    while curr.get_left_child() is not None:
        curr = curr.get_left_child()

    return curr.get_value()


def max_value(head):
    curr = head

    # loop down to find the rightmost leaf
    while curr.get_right_child() is not None:
        curr = curr.get_right_child()

    return curr.get_value()


A = Node(45)
B = Node(2)
C = Node(33)
D = Node(54)
E = Node(25)
F = Node(68)
G = Node(72)
H = Node(81)

root = insert(None, E)
root.print_tree()
print("")

insert(root, B)
root.print_tree()
print("")

insert(root, C)
root.print_tree()
print("")

insert(root, A)
root.print_tree()
print("")

insert(root, G)
insert(root, F)
insert(root, D)
insert(root, H)
root.print_tree()
print("")

print_node(lookup(root, 68))
print("")

# print_node(lookup(root, 10))
# print("")

print("Get Minimum value: ", min_value(root))

insert(root, Node(1))
print("Get Minimum value: ", min_value(root))

print("Get Maximum value: ", max_value(root))

insert(root, Node(100))
print("Get Maximum value: ", max_value(root))


def breadth_first(node):
    if node is None:
        raise Exception("No root found")

    path = []
    queue = MyQueue()
    queue.enqueue(node)

    while queue.size() > 0:
        curr = queue.dequeue()
        path.append(curr.get_value())

        if curr.get_left_child() is not None:
            queue.enqueue(curr.get_left_child())

        if curr.get_right_child() is not None:
            queue.enqueue(curr.get_right_child())

    return path


print("Breadth first Traversal of a BST: ", breadth_first(E))
print("")
print("Depth First Traversal of BST")


# Depth First Traversal of BST
def pre_order(node):
    path = []

    if node:
        path.append(node.get_value())
        path = path + pre_order(node.get_left_child())
        path = path + pre_order(node.get_right_child())

    return path


print("Pre-Order Traversal:", pre_order(E))


def in_order(node):
    path = []

    if node:
        path = path + in_order(node.get_left_child())
        path.append(node.get_value())
        path = path + in_order(node.get_right_child())

    return path


print("In-Order Traversal:", in_order(E))


def post_order(node):
    path = []

    if node:
        path = path + pre_order(node.get_left_child())
        path = path + pre_order(node.get_right_child())
        path.append(node.get_value())

    return path


print("Post-Order Traversal:", post_order(E))
