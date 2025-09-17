print ("MULTIPLICATION TABLE MAKER")
number = eval(input("Enter Number Here: "))

print ("Multiplication Table for", number,":") 

for m in range (1,11) :
    multab = number * m
    print (number, "x", m, "=", multab)