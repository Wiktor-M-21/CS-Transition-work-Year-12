age = int(input("Please input your age \n> "))


if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to Drive")
elif age == 16:
    print("You can buy lottery tickets")
elif age < 16:
    print("You can go trick or treating")
else:
    print("Error")