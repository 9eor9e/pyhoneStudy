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