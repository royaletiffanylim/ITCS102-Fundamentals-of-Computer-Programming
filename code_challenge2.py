n = int(input("Enter the amount to deposit : "))
print("Here is the breakdown of the deposited amount: ")
r = n 
T1 = r // 1000
r = r % 1000
T2 = r // 500
r = r % 500
T3 = r // 200
r = r % 200
T4 = r // 100
r = r % 100
T5 = r // 50 
r = r % 50
T6 = r // 20
r = r % 20
T7 = r // 10
r = r % 10
T8 = r // 5
r = r % 5 
T9 = r // 1
r = r % 1
print("1000 : ",T1)
print("500 : ",T2)
print("200 : ",T3)
print("100 : ",T4)
print("50 : ",T5)
print("20 : ",T6)
print("10 : ",T7)
print("5 : ",T8)
print("1 : ",T9)
