number = eval(input("Enter Number Here --> "))
f = 1

for n in range (number, 0, -1) :
	f *= n

print ("The Factorial of", number, "is", f) 