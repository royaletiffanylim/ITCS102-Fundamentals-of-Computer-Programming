
for i in range(1, 6 + 1):
    print("  " * (6 - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()