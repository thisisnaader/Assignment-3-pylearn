#input
n = int(input("Enter a number: "))

#process
#loop to print rows
for i in range(1, n+1):

    #loop to print *
    for j in range(1, n+1):
        print("*",end="")

    #line break
    print()