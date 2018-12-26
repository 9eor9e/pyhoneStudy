# 使用while循环来处理list和dictionary
# unconfirmed_users = ['alice','brian','candace'] # 创建一个待验证用户列表
# confirmed_users = [] # 创建一个用于存储已验证用户的空列表
# while unconfirmed_users: # 当待验证用户列表不为空则判断为True时不停的循环
#     current_user = unconfirmed_users.pop() # pop()函数把待验证列表末尾用户删除并存储到变量current_user中
#     print("Verifying user: " + current_user.title()) # 打印Verifying user: 加上存储在current_user中的用户名，并首字母大写
#     confirmed_users.append(current_user) # 把current_user变量中的值添加到已验证用户列表中。
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users: # 使用for循环遍历已验证用户列表里的值
#     print(confirmed_user.title()) # 打印

# 7.3.2 删除包含特定值的所有列表元素
# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# 7.3.3 使用用户输入来填充字典
responses = {}
polling_active = True # 设置一个标志，指出调查是否继续
while polling_active: # 进入while循环
    name = input("\nWhat is your name? ") # 提示输入调查用户名
    response = input("Which mountain would you like to climb someday? ") # 提示输入调查用户的回答
    responses[name] = response # 将被调查用户名存储在字典中
    repeat = input("Would you like to let another person respond? (yes / no) ") # 询问是否还有别人要参与调查，回答yes继续回答no结束
    if repeat == 'no': # 如果输入no
        polling_active = False # 循环标志赋值False，循环结束
print("\n--- poll Results ---") # 打印一行字
for name,response in responses.items(): # for遍历responses字典中的键 - 值对
    print(name.title() + " would like to climb " + response.title() + "." ) # 打印字典中的name+一句话+response