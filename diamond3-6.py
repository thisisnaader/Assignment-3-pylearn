#input
n = int(input()) #limit of starts

#process

# loop to print rows
for i in range(1, n + 1):
        
        # loop to print spaces
        for j in range (1, ((n - i) + 1)):
            print(" ", end="")
        
        # loop to print star
        for k in range(1, i + 1):
            print("*", end =" ")
        
        # line break
        print()

# loop to print rows        
for i in range(1, n):

    # loop to print spaces
    for j in range(1, i + 1):
        print(" ",end="")

    # loop to print star    
    for k in range(1, (n - i) + 1):
         print("*", end=" ")

    # line break     
    print()
