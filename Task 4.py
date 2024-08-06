import random

user = 0

heads_or_tails = ["heads","tails"]
print("Heads or Tails:")
while user != 1:
    computerchoice = random.choice(heads_or_tails)
    user_choice = input("h or t\n> ")
    if user_choice == "h":
        print("You chose heads")
        if computerchoice == "heads" and user_choice == "h":
            print("You win")
            print("Computer chose: "+computerchoice)
            leave = input("Do you want to leave? Y or N\n> ")
            if leave == "Y" or leave == "y":
                user = 1
        else:
            print("Bad Luck")
            print("Computer chose: "+computerchoice)
            leave = input("Do you want to leave? Y or N\n> ")
            if leave == "Y" or leave == "y":
                user = 1
    elif user_choice == "t":
        print("You chose tails")
        if computerchoice == "tails" and user_choice == "t":
            print("You win")
            print("Computer chose: "+computerchoice)
            leave = input("Do you want to leave? Y or N\n> ")
            if leave == "Y" or leave == "y":
                user = 1
        else:
            print("Bad luck")
            print("Computer chose: "+computerchoice)
            leave = input("Do you want to leave? Y or N\n> ")
            if leave == "Y" or leave == "y":
                user = 1
    else:
        print("Incorrect choice")

