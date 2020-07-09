import random
print("welcome to stone-paper-scissor game with computer!!","*****************************",sep="\n")
print("you can press 0 whenever you want to quit")
print("let's start the game")

while True:

        print("press 1,2,3 for indicating stone,paper,scissor respectively!!")
        turn=int(input("it's your turn ,enter your choice:"))
        comp=random.randint(1,3)
        if(turn>3):
            print("enter a valid choice")
        elif (turn==comp):
            print("match draw!")

        elif (turn==1 and comp==3) or (turn==3 and comp==2) or (turn==2 and comp==1):
            print("congratulations!! you won the match...")
        elif(turn==0):
            exit(0)

        else:
            print("you lost!! better luck next time")
