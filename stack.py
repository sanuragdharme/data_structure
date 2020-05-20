# Use Python List as stack - Last in First Out

print("*** Python List as Stack ***")
stack = []
stack.append("Cricket")
stack.append("Football")
stack.append("Baseball")

print("Stack: ", stack)

# It will removed last element - Last in First Out (LIFO)
stack.pop()
print("Stack: ", stack)
print("")

# Custom Stack
print("*** Custom Stack ***")


class Stack:
    def __init__(self):
        """ Create a new Stack """
        self.stack = []

    def push(self, item):
        """ Add element to the Stack """
        self.stack.append(item)

    def pop(self):
        """ Remove the top element of the Stack - Last In First Out (LIFO) """
        return self.stack.pop(len(self.stack) - 1)

    def is_empty(self):
        """ Return true if Stack is empty """
        return len(self.stack) == 0

    def peek(self):
        """ Have a look at top element of the stack """
        if self.is_empty():
            raise Exception("Nothing to peek")
        return self.stack[len(self.stack) - 1]

    def size(self):
        """ Return the size of stack """
        return len(self.stack)


game = Stack()
print(type(game))

game.push("Cricket")
game.push("Football")
game.push("Baseball")
game.push("Rugby")

print("Size of Stack: ", game.size())
print("Is Empty: ", game.is_empty())
print("Peek at top element: ", game.peek())
print("Remove first element: ", game.pop())
