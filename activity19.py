for k in range(1, 11, 1):
    for b in range(10, k, -1):
        print("☆", end = " ")
    for b in range(1, k, 1):
        print("♡", end = " ")
    print()
