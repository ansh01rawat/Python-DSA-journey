class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if len(self.items) == 0:
            print("queue is empty")
            return
        x = self.items.pop(0)
        return x
    def front(self):
        if len(self.items) == 0:
            print("queue is empty")
            return
        return self.items[0]
    def rear(self):
        if len(self.items) == 0:
            print("queue is empty")
            return
        return self.items[-1]
    def size(self):
        return len(self.items)


itm1 = Queue()
itm1.enqueue(12)
itm1.enqueue(13)
itm1.enqueue(14)
itm1.enqueue(15)
itm1.enqueue(16)
print(itm1.size())
itm1.dequeue()
print(itm1.front())
print(itm1.rear())
itm1.enqueue(19)
itm1.dequeue()
print(itm1.front())
print(itm1.rear())
print(itm1.is_empty())
print(itm1.size())
itm1.dequeue()
itm1.dequeue()
itm1.dequeue()
itm1.dequeue()
print(itm1.is_empty())

