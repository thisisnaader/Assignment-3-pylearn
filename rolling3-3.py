import random
import time
sum = 0

x = input("Please press enter to start rolling to Boxcars!")       #if user want to promt for start rolling, we use this variable

while sum < 12:
    
    print("Rolling the dices... 🎲🎲 ")
    #time.sleep(1)                                                  #just for better knowing we can use it
   
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6) 
    sum = dice1 + dice2
   
    print("You rolled a" ,dice1 ,"and a", dice2,". Total is: ", sum)
   
    if sum == 12:
        print("Congratulation. 🎉")
   
    else:
        print("unmatching, Tray more. ✌️")
        #x = input("Press enter to rolling.")                       #if user want to promt for ech rolling, we use this variable

