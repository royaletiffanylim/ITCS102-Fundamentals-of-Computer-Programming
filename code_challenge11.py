print("\t\t ✮", end = "")
for k in range(1, 11, 1):
    for c in range(10, k, -1):
        print(" ", end = " ")
    for d in range(1, k, 1):
        print("✦", end = " ")
    for e in range(1, k, 1):
        print("✦", end = " ")
    print()