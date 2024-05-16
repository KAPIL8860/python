import random

Target = random.randint(1 ,100)
print()

while True :
    userChoice =  input("Guess the Target or Quit(Q) :")
    if (userChoice == "Q") :
          break
    userChoice = int(userChoice)
    if (userChoice == Target) :
        print("Success : Correct Guess!!")
        break
    elif(userChoice < Target) :
        print("your number was too small. take a bigger guess...")
    else :
                print("your number was too big. take a smaller guess...")

    print("-------GAME OVER---------")

