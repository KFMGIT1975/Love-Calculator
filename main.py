print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_1 = name1.lower()
name2_1 = name2.lower()
name = name1_1+name2_1
a_1=name.count("t")
a_2=name.count("r")
a_3=name.count("u")
a_4=name.count("e")
b_1=name.count("l")
b_2=name.count("o")
b_3=name.count("v")
b_4=name.count("e")
a=a_1+a_2+a_3+a_4
b=b_1+b_2+b_3+b_4

score=int(str(a)+str(b))
if (score<10) or (score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
