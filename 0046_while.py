# while循环 - 示例1
# current_number = 1 # 变量赋值1
# while current_number <=5: # 当该变量小于等于5时不断循环
#     print(current_number) # 每一次循环都把该变量的值打印出来
#     current_number += 1 # 每循环一次，该变量的值都+1

# while循环示例2 - 让用户决定程序什么时候结束。
# prompt = "\nTell me something,and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != "quit":
#     message = input(prompt)
#     print(message)

# while循环示例3 - 示例2改进，不显示quit字符。
# prompt = "\nTell me something,and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message)

# 使用标志
# prompt = "\nTell me something,and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# 使用break退出循环
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# 循环中使用continue
current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)