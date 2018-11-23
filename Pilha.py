class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        return self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return ("Pilha vazia")
        else:
            return self.stack.pop()

    def printStack(self):
        y = []
        for x in self.stack:
            y.append(x.nome)
        return y

    def size(self):
        return len(self.stack)