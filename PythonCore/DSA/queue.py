from collections import deque
class Queue:
    def __init__(self):
        self.items=deque()
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return "Queue under flow"
        return self.items.popleft()
    def peek(self):
        if self.items.is_empty():
            return "Queue is empty"
        return self.items[0]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
def main():
    q=Queue()
    q.enqueue(10)
    print(q.size())
    print(q.dequeue())
if __name__=="__main__":
    main()