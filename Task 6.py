import random

valid_choice = 0


def addition_sub():
    ran_num1 = random.randint(5,26)
    ran_num2 = random.randint(5,26)
    user_answer = int(input(str(ran_num1)+"+"+str(ran_num2)+"\n> "))
    ans = ran_num1+ran_num2
    print(user_answer)
    print(ans)
    checkanswer(user_answer,ans)

def subtraction_sub():
    ran_num1 = random.randint(25,51)
    ran_num2 = random.randint(1,26)
    user_answer = int(input(str(ran_num1)+"-"+str(ran_num2)+"\n> "))
    ans = ran_num1-ran_num2
    print(user_answer)
    print(ans)
    checkanswer(user_answer,ans)

def checkanswer(user_answer,ans):
    if int(user_answer) == int(ans):
        print("Correct")
    else:
        print("Incorrect the answer is "+str(ans))

while valid_choice != 1:
    menu_options=input("Please select an option: \n 1.Addition \n 2.Subtraction \n> ")
    if menu_options == "1":
        valid_choice = 1
        addition_sub()

    elif menu_options == "2":
        subtraction_sub
        valid_choice = 1
    else:
        print("This option is unavailable")