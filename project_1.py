# Rock, paper, scissors game using numpy in python (project -> 1)

import numpy as np

user = input("Enter your choice (r/p/s): ").lower().strip()
choice = np.array(["r","p","s"])
computer = np.random.choice(choice)
print("Computer chose:", computer)
if user == computer:
    print("Tie")
else:
    if user == "r" and computer == "p" or user == "p" and computer == "r":
        print("whoever take the paper(p),is win")
        if user == "p":
            print("You win the game!")
        else:
            print("Computer wins the game!")

    elif user == "p" and computer == "s" or user == "s" and computer == "p":
        print("whoever take the sessior(s),is win")
        if user == "s":
            print("You win the game!")
        else:
            print("Computer wins the game!")

    elif user == "r" and computer == "s" or user == "s" and computer == "r":
        print("whoever take the rock(r),is win")
        if user == "r":
            print("You win the game!")
        else:
            print("Computer wins the game!")

    else:
        print("invalid")
