for i in range(1, 11,1):
    for x in range(10, i, -1):
        print(" ", end = " ")
    for y in range(1, i, 1):
        print("ꔫ", end = " ")
    for z in range(1, i, 1):
        print("ꔫ", end = " ")
    print()
    
    #print("\t\t *", end="")
for i in range(1, 11,1):
    for x in range(1, i, 1):
        print(" ", end = " ")
    for y in range(10, i, -1):
        print("ꔫ", end = " ")
    for z in range(10, i, -1):
        print("ꔫ", end = " ")
    print()