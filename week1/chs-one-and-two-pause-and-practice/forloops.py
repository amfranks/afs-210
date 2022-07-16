# for <variable> in [sequence of data]:

def countDown():

	for currentCount in [5, 4, 3, 2, 1]:
		print(currentCount)
			
	print("BLAST OFF!")
	
countDown()

###########################################################

def welcomeGuests(guestNames):

	for guest in guestNames:
		print("Welcome",guest)
		

guests = []
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))

welcomeGuests(guests)

###########################################################

# range(start, stop[, step])

# start
# The value of the start parameter (or 0 if the parameter was not supplied)

# stop
# The value of the stop parameter

# step
# The value of the step parameter (or 1 if the parameter was not supplied)

def count(stop):
    for number in range(1, stop+1, 1):
        print(number)

stoppingNum = int(input("Count to? "))
count(stoppingNum)

###########################################################

def countDown(start):

	for currentCount in range(start,0,-1):
		print(currentCount)
			
	print("BLAST OFF!")
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)