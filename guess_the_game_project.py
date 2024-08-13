import random

target= random.randint(1,100)

while True:
    userChoice = input("Guess the number or Quit(Q):")
    if(userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success : Correct guess!")
        break
    elif(userChoice < target): 
        print("Your Guess is too Small. Guess a bigger number")
    else:
        print("Your Guess is too big. Guess a smaller number")

print(" ____GAME OVER____")