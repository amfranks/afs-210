class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        # Insert your hashing function code
        return key % self.size

    def rehash(self, key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self, key, data):
        # Insert your code here to store key and data
        h = self.hashfunction(key)
        if self.data[h] == None: 
            self.slots[h] = key
            self.data[h] = data
        else:
            if (self.slots[h] == key):
                self.data[h] = data
            else:
                h = self.rehash(key)
                if(self.data[h] == None):
                    self.slots[h] = key
                    self.data[h] = data
                else:
                    return None

    def get(self, key):
        # Insert your code here to get data by key
        h = self.hashfunction(key)
        while self.slots[h] is not None: # While the slots are not empty
            if self.slots[h] is key:
                return self.data[h] # Return key if value is found
            # h = (h + 1) % self.size 
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()

# Store remaining input data
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)

# print the data values
print(H.data)

# print the value for key 52
print(H[52])