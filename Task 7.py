import random

def get_low_high():
    low = int(input("Enter the low number: "))
    high = int(input("Enter the high number: "))
    comp_num = random.randint(low, high)
    return comp_num

def guess_number():
    print("I am thinking of a number...")
    user_guess = int(input("Guess the number: "))
    return user_guess

def check_guess(comp_num):
    while True:
        user_guess = guess_number()
        if user_guess == comp_num:
            print("Correct, you win!")
            break
        elif user_guess < comp_num:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

def main():
    comp_num = get_low_high()
    check_guess(comp_num)

main()
