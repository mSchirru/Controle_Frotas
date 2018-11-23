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
        y = []
        for x in self.queue:
            y.append(x.nome)
        return y

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def return_queue(self):
        return self.queue