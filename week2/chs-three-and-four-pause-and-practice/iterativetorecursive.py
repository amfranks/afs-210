def countDown():
    for i in range(10, 0, -1):
        print(i)
    print("Blast Off!!!")

countDown()

#Three Parts of a Recursive Algorithm
#1. Must have a base case – base case stops the recursion
#2. Must move towards the base case by changing the state
#3. Recursively call itself

def blastOff(i):
    if (i == 0):
        print("Blast Off!!!")
    else:
        print(i)
        blastOff(i - 1)

blastOff(10)