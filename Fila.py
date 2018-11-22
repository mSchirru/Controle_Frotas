class Queue(object):
    def __init__(self):
        self.queue = []
        self.tail = 0

    def enqueue(self, data):
        self.queue.insert(self.tail, data)
        self.tail += 1

    def dequeue(self):
        self.queue.pop()

    def printQueue(self):
        return self.queue