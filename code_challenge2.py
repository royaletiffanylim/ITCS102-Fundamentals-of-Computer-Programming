n = int(input("Enter the amount to deposit : "))
print("Here is the breakdown of the deposited amount: ")
r = n 
d1 = r // 1000
r = r % 1000
d2 = r // 500
r = r % 500
d3 = r // 200
r = r % 200
d4 = r // 100
r = r % 100
d5 = r // 50 
r = r % 50
d6 = r // 20
r = r % 20
d7 = r // 10
r = r % 10
d8 = r // 5
r = r % 5 
d9 = r // 1
r = r % 1
print("1000 : ",d1)
print("500 : ",d2)
print("200 : ",d3)
print("100 : ",d4)
print("50 : ",d5)
print("20 : ",d6)
print("10 : ",d7)
print("5 : ",d8)
print("1 : ",d9)
