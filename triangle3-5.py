#input

n = int(input())

#process

#loop to print rows
for i in range(1, n + 1):

    #loot to print space
    for j in range(1, (n - i) + 1):
        print(" ",end="")

    #loop to print stars    
    for k in range(1, i + 1):
        print("* ",end="")

    #line break    
    print()
