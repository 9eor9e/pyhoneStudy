# input()函数 - 示例1
# message = input("Tell me something, and I will repeat"
#                 " it back to you: ")
# print(message)

# input()函数 - 示例2
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# input()函数 - 示例3
# prompt = "If you tell us who are you,we can personalize the message you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print("\nHello, " + name + "!")

# input()函数和int()函数 - 示例4
# age = input("How old are you? ") # 使用input()函数输入的数字默认是字符串格式
# print(type(age))

# input()函数和int()函数 - 示例5
# age = input("How old are you? ")
# # age = int(age)
# # age >=18
# # print(age)

# input()函数和int()函数 - 示例6
height = input("How tall are you, in inches? ")
height = int(height) # 将age变量数据转换成数值类型
if height >=36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")