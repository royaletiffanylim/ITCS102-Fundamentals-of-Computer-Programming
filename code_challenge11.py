print("\t\t ✮", end = "")
for r in range(1, 11, 1):
    for t in range(10, r, -1):
        print(" ", end = " ")
    for p in range(1, r, 1):
        print("✦", end = " ")
    for l in range(1, r, 1):
        print("✦", end = " ")

    print()
