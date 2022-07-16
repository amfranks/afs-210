def countDown(start):

	while start > 0:
		print(start)
		start -= 1
			
	print("BLAST OFF!")
	
startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

####################################################################

def countDown(start):
	continueLoop = True
	while continueLoop:
		print(start)
		start -= 1
		if (start == 0):
			print("BLAST OFF!")
			continueLoop = False	
	

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

####################################################################

def countDown(start):
    while True:
        print(start)
        start -= 1
        if (start == 0):
            print("BLAST OFF!")
            break

startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)