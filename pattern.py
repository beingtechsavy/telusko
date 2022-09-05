for j in range (5):
    for i in range(5-j):
        print("$ ", end="")
    print()

for j in range (1,4):
    for i in range(1,5):
        if (i%2==0):
            print("&",end ="")
        else:
            print("_")
    print()
