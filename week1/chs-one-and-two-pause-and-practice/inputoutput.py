print('Hello world')

print('Mary Shelley wrote "Frankenstein" in 1818') # Double quotes within string.
print("""Mary Shelley wrote "Frankenstein" in 1818""") # Quotes within string.
print("Mary Shelley wrote \"Frankenstein\" in 1818") # Quotes within string.

print("I have meetings this week on \
      Monday, Tuesday, and Friday")

applesSold = 10
applePrice = 0.20

print("We sold",applesSold,"apples at $",applePrice,"each for a total of $",(applesSold * applePrice), sep=" ")

applesSold = 5000
applePrice = 0.20

print("We sold ",applesSold," apples at $",
format(applePrice,',.2f'),\
" each for a total of $",\
format((applesSold * applePrice),',.2f'),\
sep="")

applesSold = int(input("How many apples did you sell this week? "))
applePrice = float(input("What the price of each apple sold? "))
print("You sold ",applesSold," apples at $",applePrice," each for a total of $",(applesSold * applePrice), sep="")