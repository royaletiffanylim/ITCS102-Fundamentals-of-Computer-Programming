name = input("Please, Enter Your Name Here --> ")
fare = eval(input("Enter Fare Fee --> "))
isStudent = input("Are you currently a student? (yes / no) ")

if isStudent == 'yes':
	discount = fare * 0.2
	#fare -= discount
	new_fare = fare - discount
	print("Hi ", name)
	print("Your Discount is ", discount)
	print("Your New Fare is ", new_fare)
else: 
	print("We're sorry", name, "You are not eligible for a Student Discount")