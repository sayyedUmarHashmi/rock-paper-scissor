import random
options=["rock","paper","scissor"]

relentless=True
while relentless:
    human=None
    computer=random.choice(options)

    while human not in options:
        human=input("Enter your choice:")
    print(f"player choice is {human} and computer choice is {computer}")
    if computer==human:
            print("Oh god it\'s a draw")
    elif computer.startswith("r") and human.startswith("s"):
            print("Alas! you have lost the game")
    elif computer.startswith("p") and human.startswith("r"):
            print("you have lost the game but won the rock")
    elif computer.startswith("s") and human.startswith("p"):
            print("you are a losser ")
    else:
            print("Oh wow you have won it!")

    kaif=input("do you wanna play again(y/n):")
    if kaif!="y":
           relentless==False
           break
print("after all that relentless night i finally did it, fuck you!")
