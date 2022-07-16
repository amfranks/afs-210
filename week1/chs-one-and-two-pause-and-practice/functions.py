# A function is a block of code that exist within a program designed to perform a specific task.

# When defining the name of a function, you must follow the same naming rules as those for variables.

# There are rules when naming functions / variables and include:
# • You cannot use one of Python’s key words as a functions / variable name. 
# • A functions / variable name cannot contain spaces.
# • The first character must be one of the letters a through z, A through Z, or an underscore character (_).
# • After the first character you may use the letters a through z or A through Z, the digits 0 through 9, or underscores.
# • Uppercase and lowercase characters are distinct. 

def classMessage():
    print("AFS-210", end=" : ")
    print("Data Structures and Algorithms")

print("Welcome to:")
classMessage()
print("I hope you enjoy your next eight weeks of class.")

#####################################################################

applesSold = 10
applePrice = 0.20

def showAppleTax():
	taxRate = 0.06
    # applesSold = 50
	appleTax = (applesSold * applePrice) * taxRate
	print("The tax on the sale of",applesSold,"apples is",appleTax)
	
showAppleTax()	

print(applesSold)

#####################################################################

def showSum(a, b = 0):
    print(a + b)

x = 1 # x is the pointer (to the memory location) to where the value of 1 is stored.
y = 3
showSum(x, y)
showSum(x) # 1 + 0 = 1

#####################################################################

def sum(a, b):
	return a + b

y = sum(1, 2)
print(y) # 3

#####################################################################

def add_subtract(a, b):
	return a + b, a - b
	
sum, sub = add_subtract(1, 2)
print(sum)
print(sub)	