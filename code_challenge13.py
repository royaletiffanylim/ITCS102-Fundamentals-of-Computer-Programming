print ("WELCOME TO SUMMATION OF ODD NUMBERS!!!")
name = input("Please, Enter Your Name Here: ")
print("++++++++++++++++++++++++++++++++++++++++ \nODD NUMBER SUMMATION, Enter 0 to Stop\n++++++++++++++++++++++++++++++++++++++++")
tiff = True
sum = 0
odd = ""

while tiff == True:
      number = eval(input("Input a random number -->  ")) 
     
      if number % 2 == 1:
            print("ODD NUMBER DETECTED, continue ")
            sum += number
            odd += str(number) + " "
            continue
      elif number == 0:
            print("SYSTEM STOPPED!!!") 
            break
      else:
            if number % 2 == 0:
                 print("EVEN NUMBER, continue ")
            else:
                 print("NUMBER INVALID")
            continue
print(f"Thank You {name}, The Sum of All ODD NUMBER is {sum} ")
print(f"ODD NUMBERS detected are {odd}") 