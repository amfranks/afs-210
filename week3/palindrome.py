class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() 

    def size(self):
        return len(self.items)   

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]
    

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []

    def peek(self):
        if (len(self.queue) >= 1):
            print(self.queue[len(self.queue) - 1])
        else:
            print("List is empty")

def is_palindrome(str):
    stack = Stack()
    queue = Queue()

    for i in str:
        stack.push(i)
        queue.enqueue(i)

    while not stack.isEmpty():
        if stack.pop() != queue.dequeue():
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("noon"))
print(is_palindrome("python"))
print(is_palindrome("madam"))