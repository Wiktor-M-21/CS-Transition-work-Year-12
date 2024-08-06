total = 0

for i in range (5):
    user_num = int(input("Enter a number \n> "))
    y_or_n = input("Do you want to add the number to the total y or n \n> ")
    if y_or_n == "y":
        print("Done")
        total=total+user_num
print("Total is: "+total)