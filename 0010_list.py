# list列表，格式为[vaule,vaule......]

# 创建list，并打印
numbers = ['1', '2', '3', '4', '5', '6', ]
print(numbers)

# 打印出list中指定的值,索引从0开始而不是1
print(numbers[1])

# 使用-1来索引list中最后一个值
print(numbers[-1])

# 使用list中的值做加法(好像不能做加法，list保存的数据类型是str)
message = 'list里的值相加等于 = ' + numbers[1] + numbers[-1]
print(type(numbers[1]))
print(message)

# list练习1
names = ['王二','张三','李四','赵五','小明']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# list练习2
massage_1 = 'Welcome, ' + names[0] + ' !'
massage_2 = 'Welcome, ' + names[1] + ' !'
massage_3 = 'Welcome, ' + names[2] + ' !'
massage_4 = 'Welcome, ' + names[3] + ' !'
massage_5 = 'Welcome, ' + names[4] + ' !'
print(massage_1)
print(massage_2)
print(massage_3)
print(massage_4)
print(massage_5)