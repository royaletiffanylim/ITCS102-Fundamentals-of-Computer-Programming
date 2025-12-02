import os
import json

print("STUDENT INFORMATION SYSTEM")

student_records = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - IMPORT STUDENT RECORD")
    print("X - EXIT STUDENT RECORD")

    choice = input("SELECT FROM THE OPTIONS ABOVE: ").lower()

    if choice == 'a':
        print("\nADDING NEW RECORD")
        new_info = []
        id_no = input("Enter ID Number: ")
        first_name = input("Enter First Name: ").upper()
        last_name = input("Enter Last Name: ").upper()
        age = input("Enter Your Age: ").upper()
        section = input("Enter Your Section: ").upper()
        course = input("Enter Your Current Course: ").upper()

        student_records[id_no] = [first_name,last_name,age,section,course]
        print("RECORD SAVED SUCCESSFULLY")
        continue
    
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        
        for i, j in student_records.items():
            print(f"{i} : {j}")
        continue
    elif choice == 'c':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Input Student ID: ").lower()
        
        for each_id in student_records.keys():
            if search_id in student_records.keys():
                print(f"\nRECORD FOUND FOR {search_id}")
                for i in student_records[search_id]:
                    print(f" --- {i}")
            else:
                print("\n\nNO RECORD FOUND FOR {search_id}")
            break
        continue
    elif choice == 'd':
        os.system('cls')

        print("DELETE STUDENT RECORD")

        search_id = input("Input Student ID: ").lower()
        
        for each_id in student_records.keys():
            if search_id in student_records.keys():
                print(f"\nRECORD FOUND for ID {search_id}")

                for i in student_records[search_id]:
                    print(f" --- {i}")

                student_records.pop(search_id)
                print("\nRECORD DELETED")
            else:
                print("\n\nNO RECORD FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Input Student ID: ").lower()
        
        for each_id in student_records.keys():
            if search_id in student_records.keys():
                print(f"\nRECORD FOUND for {search_id}")
                for i in student_records[search_id]:
                    print(f" --- {i}")
                id_no = input("Enter ID Number: ")
                first_name = input("Enter First Name: ").upper()
                last_name = input("Enter Last Name: ").upper()
                age = input("Enter Your Age: ").upper()
                section = input("Enter Your Section: ").upper()
                course = input("Enter Your Current Course: ").upper()


                student_records[search_id][0] = first_name
                student_records[search_id][1] = last_name
                student_records[search_id][2] = age
                student_records[search_id][3] = section
                student_records[search_id][4] = course

                print("DATA UPDATED")
            else:
                print("NO RECORD FOUND")        
            break
        continue
    elif choice == 'f':
        os.system('cls')
        print("EXPORT STUDENT DATA")

        with open('student_records.json', 'w') as new_file:
            json.dump(student_records,new_file, indent=4 )

        print("\nDATA EXPORTED TO JSON")
        continue
    elif choice == 'g':
        os.system('cls')
        print("IMPORT STUDENT DATA")

        with open('student_records.json', 'r') as new_file:
            imported_student = json.load(new_file)

        student_record = imported_student
        print("\nDATA IMPORTED TO JSON")
        continue
    elif choice == 'x':
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE, RE-ENTER YOUR CHOICE")
        continue