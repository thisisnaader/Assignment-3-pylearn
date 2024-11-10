import time
n = int(input("Enter the number of seconds for countdown: "))


while n != 1:
    print(n," seconds remaining... ⏱️")
    time.sleep(1)
    n -= 1

print("Time's up")


