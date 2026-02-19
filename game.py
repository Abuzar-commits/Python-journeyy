import random
choices=["rock","paper","scissors"]
while True:
    user=input("Enter your Choice (rock,papers,scissors or quit to end the game)
               : ").lower()
    if user=="quit":
        print("Game ended")
        break
    if user not in choices:
        print("Invalid Choice ! Try Again.")
        continue
    computer=random.choice(choices)
    print("Computer choose:",computer)

    if user==computer:
        print("Its a Tie!")
    elif(user=="rock" and computer=="scissors")or(user=="scissors"and computer=="paper")or(user=="paper" and computer=="rock"):
        print("You win")
    else:
        print("Computer wins")

