import random

points = 0
print("Maths Quiz")
for i in range(5):
    random_math = ["add","subtract","multiply"]
    math_func = random.choice(random_math)
    if math_func == "add":
        num1=random.randint(1,10000)
        num2=random.randint(1,10000)

        userans = input(str(num1)+"+"+str(num2)+"\n> ")
        ans = num1+num2
        if int(userans) == int(ans):
            print("Correct \n+1 point")
            points=1+points
        else:
            print(ans)
    elif math_func == "subtract":
        num1=random.randint(1,10000)
        num2=random.randint(1,10000)
        if num1 > num2:
            userans = input(str(num1)+"-"+str(num2)+"\n> ")
            ans = num1-num2
            if int(userans) == int(ans):
                print("Correct \n+1 point")
                points=1+points
            else:
                print(ans)
        elif num1 < num2:
            userans = input(str(num2)+"-"+str(num1)+"\n> ")
            ans = num2-num1
            if int(userans) == int(ans):
                print("Correct \n+1 point")
                points=1+points
            else:
                print(ans)
    elif math_func == "multiply":
        num1=random.randint(1,13)
        num2=random.randint(1,13)
        userans = input(str(num1)+"x"+str(num2)+"\n> ")
        ans = num1*num2
        if int(ans) == int(userans):
            print("Correct \n+1 point")
        else:
            print(ans)
    else:
        print("error")

print("You have gotten: "+str(points)+" points")
    