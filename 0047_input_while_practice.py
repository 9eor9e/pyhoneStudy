# input()和while - 练习1
# prompt = "\nPlease enter the topping in your pizza."
# prompt += "\nIf you enter 'quit' the program will finished."
# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(topping.title() + " will add!")

# input()和while循环 - 练习2
# prompt = "\nPlease enter your age,thanks."
# prompt += "\nWe will tell you how much the ticket!"
# age = input(prompt)
# age = int(age)
# while True:
#     if age < 3 :
#         print("It's free for you!")
#         break
#     elif age <= 12 :
#         print("Please pay 10$ .")
#         break
#     else :
#         print("Please pay 15$ .")
#         break

# input()和while循环 - 练习3
prompt = "\nPlease enter your age,thanks."
prompt += "\nWe will tell you how much the ticket!"
age = input(prompt)
age = int(age)
active = True
while active:
    if age < 3 :
        print("It's free for you!")
        active = False
    elif age <= 12 :
        print("Please pay 10$ .")
        active = False
    else :
        print("Please pay 15$ .")
        active = False