# list的练习

# 创建vip_list，并打印
vip_list = ['张三','李四','赵五','小陆']
print(vip_list[0] + ',can i have dinner with you?')
print(vip_list[1] + ',can i have dinner with you?')
print(vip_list[2] + ',can i have dinner with you?')
print(vip_list[3] + ',can i have dinner with you?')

# 小陆不能出席
no_time_name = '小陆'
vip_list.remove(no_time_name)
print(vip_list)

# 邀请阿七替换小陆
vip_list.append('阿七')
print(vip_list)
print(vip_list[3] + ',can i have dinner with you?')
print(no_time_name + ",she can't have dinner,because no time.")