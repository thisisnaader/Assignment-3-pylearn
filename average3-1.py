n = int(input("N: "))
i = 1
scores = 0
if n == 0:
    print ("0")
else:
    while i <= n:
        score = int(input("Enter score: "))
        scores += score
        i +=1
    avg = scores / n
    print("average is: ", avg)
