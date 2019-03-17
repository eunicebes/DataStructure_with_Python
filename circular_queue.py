class CircularQueue:

    def __init__(self):
        self.queue = [None] * 100
        self.head = 0
        self.tail = 0
        self.number_of_items = 0
        self.max_size = len(self.queue)

    def enqueue(self, data):
        if self.number_of_items == 0:
            self.head = self.tail = 0
            self.queue[0] = data
        else:
            self.tail = (self.tail + 1) % self.max_size
            self.queue[self.tail] = data

        self.number_of_items += 1

    def dequeue(self):
        if self.number_of_items == 0:
            return ("Queue Empty!")

        remove = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        self.number_of_items -= 1
        return remove
