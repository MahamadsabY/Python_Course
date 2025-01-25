import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 1, 0])
yourstr = input("Enter your choice : ")
youDict = {"s":1, "w": -1, "g":0}
reverseDict = {1 : "Snake", -1:"Water", 0 : "Gun"}

you = youDict[yourstr]

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if(computer == you):
    print("its a tie")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Loose!")

    elif(computer == 1 and you == -1):
        print("You Loose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Loose!")

    else:
        print("something went wrong..!")    