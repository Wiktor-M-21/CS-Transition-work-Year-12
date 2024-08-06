name = input("Enter your name \n> ")
num = int(input("Enter a number\n> "))

if num < 10:
    for i in range (num):
        print(name)
else:
    for i in range (3):
        print("Too high")