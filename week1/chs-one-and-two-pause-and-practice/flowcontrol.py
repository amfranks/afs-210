# Operator Meaning
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

def buy2Get1Free(qnty):
	if qnty >= 6:
		print("You qualify for multiple the Buy 2 Get 1 Free Discounts")
	elif (qnty >= 3) and (qnty < 6):
		print("You get one Apple for Free!")
	else:
		print("You do not quality for the discount")


applesSold = 6

buy2Get1Free(applesSold)
