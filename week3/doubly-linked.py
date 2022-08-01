# A doubly-linked node.
from turtle import pos


class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

# A doubly-linked list.
class DoublyLinkedList:
    def __init__(self): # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    # Iterate through the list.
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    # Returns the number of elements in the list
    def size(self) -> int:
        return self.count

    # Add a node at the front of the list.
    def addFirst(self, data) -> None:
        node = Node(data) 
        if (self.head == None): 
            self.head = node
            return
        else: 
            self.head.prev = node
            node.next = self.head
            self.head = node

    # Add a node to the end of the list.
    def addLast(self, data) -> None:
        node = Node(data)
        if (self.head == None):
            self.head = node
            return
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = node
            node.prev = temp
        self.count += 1
        
    # Add a node to the list at the given index position
    # If index equals to the length of linked list, the node will be appended to the end of linked list
    # If index is greater than the length, the data will not be inserted.
    # This function does not replace the data at the index, but pushes everything else down.
    def addAtIndex(self, data, index):
        node = Node(data)
        temp = self.head
        for i in range(1, index):
            temp = temp.next
        node.prev = temp
        node.next = temp.next
        temp.next.prev = node
        temp.next = node
        self.count += 1
        
    def indexOf(self, data):
    # Search through the list. Return the index position if data is found, otherwise return -1.
        temp = self.head
        found = 0
        i = 0
        while (temp != None):
            if (temp.data == data):
                found += 1
                break
            i += 1
            temp = temp.next
        if (found == 1):
            return i
        else:
            print("data not found")
            return -1

    def add(self, data) -> None:
        # Append an item to the end of the list.
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list.
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ " "
            # print("test")
        return myStr

dll = DoublyLinkedList()

dll.add("May")
dll.add("the")
dll.add("Force")
dll.add("be")
dll.add("with")
dll.add("you")
dll.add("!")

print(dll.__str__())
print(dll.indexOf("with"))
dll.__setitem__(5, "us")
dll.addAtIndex("all", 6)
print(dll.__str__())