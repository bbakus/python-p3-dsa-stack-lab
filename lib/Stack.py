class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
        

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
            return True
        else:
            return False 

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        for i in range(len(self.items)):
            if self.items[i] == target:
                
                return len(self.items) - 1 - i
        return -1
