# Sum the odd numbers between 1 and 20
def loop1():
    odd_sum = 0

    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i

    return odd_sum

# Duplicate the loop1 function using recursion
def loop1Rec(start, stop, odd_sum = 0):

    # Base case
    if start >= stop:
        return odd_sum

    # Recursive call
    if (start % 2) == 1:
        return loop1Rec(start + 1, stop, odd_sum + start)
    else:
        return loop1Rec(start + 1, stop, odd_sum)

###########################################################

# Sum the even numbers between 1 and 20
def loop2():
    i = 0
    even_sum = 0

    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1

    return even_sum

# Duplicate the loop2 function using recursion
def loop2Rec(start, stop, even_sum = 0):

    # Base case
    if start >= stop:
        return even_sum

    # Recursive call
    if (start % 2) == 0:
        return loop2Rec(start + 1, stop, even_sum + start)
    else:
        return loop2Rec(start + 1, stop, even_sum)

print(loop1Rec(1, 20))
print(loop2Rec(1, 20))