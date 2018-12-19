# input()函数 - 练习1
# message = input("How about car you want to lease? ")
# print(message + "\nLet me see if I can find you a subaru.")

# input()函数 - 练习2
# number_of_people = input("How many people will go to dinner?")
# number_of_people = int(number_of_people)
# if number_of_people >8:
#     print("Sorry,we have no seats!")
# else:
#     print("Welcome!")

# input()函数和%求模运算符 - 练习3
number = input("Please enter a number, I can tell you the number 是不是整数倍。")
number = int(number)
if number % 10 ==0:
    print("This number 是10的整数倍！")
else:
    print("This number is not 10的整数倍。")