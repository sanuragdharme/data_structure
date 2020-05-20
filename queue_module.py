# Queue - First in First Out

from queue import Queue

# Built-in Queue
print("*** Built-in Queue ***")
game = Queue(5)
print("This will print object: ", game)

game.put("Cricket")
game.put("Hockey")
game.put("Football")

print("Check is Queue is empty or not: ", game.empty())
print("Check is Queue is full or not: ", game.full())
print("Queue Size {} and its max size is {}".format(game.qsize(), game.maxsize))

# To remove the data from the Queue - First In First Out (FIFO)
print("Who got removed: ", game.get())
print("")

# Custom Queue
print("*** Custom Queue ***")


class MyQueue:
    def __init__(self):
        """ Create a new queue. """
        self.items = []

    def is_empty(self):
        """ Returns true if queue is empty """
        return len(self.items) == 0

    def enqueue(self, item):
        """ Add a new element to the end of queue """
        self.items.append(item)

    def dequeue(self):
        """ Remove an element form the beginning of queue - First in First Out (FIFO) """
        try:
            return self.items.pop(0)
        except IndexError:
            print("Nothing to get bored with haha..")

    def size(self):
        """ Returns the size of the queue """
        return len(self.items)

    def peek(self):
        """ Have a look at first element of the queue """
        if self.is_empty():
            raise Exception("Nothing to peek")
        return self.items[0]


game = MyQueue()
print(game)

game.enqueue("Cricket")
game.enqueue("Hockey")
game.enqueue("Football")

print("Check is Custom Queue is empty or not: ", game.is_empty())
print("Custom Queue Size {}".format(game.size()))
print("Let's look at the 1st element the game: ", game.peek())
print(f"Ahh I am bored with {game.dequeue()} game, I don't want to play.")
print(f"Ahh I am bored with {game.dequeue()} game, I don't want to play.")
print(f"Ahh I am bored with {game.dequeue()} game, I don't want to play.")
print("Custom Queue Size {}".format(game.size()))
print(f"Ahh I am bored with {game.dequeue()} game, I don't want to play.")
