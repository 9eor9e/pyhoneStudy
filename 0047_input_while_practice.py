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
prompt = "\nPlease enter your age,thanks."
prompt += "\nWe will tell you how much the ticket!"
while True:
    age = input(prompt)
    age = int(age)
    if age < 3 :
        print("It's free for you!")
    elif age <= 12 :
        print("Please pay 10$ .")
    else :
        print("Please pay 15$ .")