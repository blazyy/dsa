class Queue:
    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def get_size(self):
        return len(self.items)

    def get_front(self):
        return self.items[0]
    
