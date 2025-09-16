temp = eval(input("Enter Temperature Here --> "))

if temp <= 0 :
	print("Temperature is Below Freezing")

if temp >= 1 and temp <= 15 :
	print("Temperature is Extemely Cold")

if temp >= 16 and temp <= 30 :
	print("Temperature is Cold")

if temp >= 31 and temp <= 38 :
	print("Temperature is Lukewarm")

if temp >= 39 and temp <= 42 :
	print("Temperature is Warm")

if temp >= 43 and temp <= 50 :
	print("Temperature is Hot")

if temp >= 51 and temp <= 60 :
	print("Temperature is Extremely Hot")

if temp >= 60 :
	print("Temperature is Burning")
