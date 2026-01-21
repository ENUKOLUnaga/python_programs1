class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return "Stack Under Flow"
        self.items.pop()
    def peek(self):
        if self.is_empty():
            return "Empty stack"
        return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    
def main():
    s=Stack()
    s.push(9)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s.size())
if __name__=="__main__":
    main()
