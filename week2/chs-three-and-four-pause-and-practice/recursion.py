# The factorial function says to multiply all whole numbers from a chosen number down to 1.
# if n = 3, then we have 3 * 2 * 1 = 6
# If n = 5, then we have 5 * 4 * 3 * 2 * 1 = 120
# If n = 8, then we have 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320

# Three Parts of a Recursive Algorithm
    # 1. Must have a base case – base case stops the recursion
    # 2. Must move towards the base case by changing the state
    # 3. Recursively call itself

# Iterative loop factorial function

def factorialLoop(x):
    retVal = x
    for i in reversed(range(1, x)):
        retVal *= i
    return retVal

# Recursive factorial function

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

n = 5
print(factorialLoop(n))
print(factorial(n))