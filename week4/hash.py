class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self) -> None:
        self.size = 255
        self.slots = [None] * self.size
        self.count = 0

    def hashFunction(self, key):
        keystr = str(key)
        hashVal = 0
        for ch in str(keystr):
            hashVal += ord(ch)

        return (hashVal * len(keystr)) % self.size

    def rehashFunction(self, key):
        keystr = str(key)
        hashVal = 0
        counter = 0
        for ch in str(keystr):
            counter += 1
            hashVal += ord(ch) + counter

        return (hashVal * len(keystr)) % self.size

    def put(self, key, value):
        # Store key:value pair
        return
    
    def get(self, key):
        # Get value for key
        return

ht = HashTable()

print(ht.hashFunction('John Smith'))
print(ht.hashFunction('Jane Doe'))
print(ht.hashFunction('George Washington'))
print(ht.hashFunction('Mike Adams'))
print(ht.hashFunction('Robert Kohlbus'))
print(ht.hashFunction('Alexander Hamilton'))
print(ht.hashFunction(4567))
print(ht.hashFunction(7654))
print(ht.rehashFunction(7654))