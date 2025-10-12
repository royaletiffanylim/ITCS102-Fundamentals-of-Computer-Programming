
for m in range(1, 6 + 1):
    print("  " * (6 - m), end="")
    for n in range(m, 0, -1):
        print(n, end=" ")
    for n in range(2, m + 1):
        print(n, end=" ")

    print()
