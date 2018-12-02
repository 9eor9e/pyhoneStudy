# 函数range()

# # 注意函数range()的差一行为，这个只能从1输出到4。
# for value in range(1,5):
#     print(value)
#
# # 使用函数range()创建数字list
# numbers = list(range(1,6))
# print(numbers)

# 使用函数range()创建数字list,打印1-10内的偶数。
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 创建一个1-10的平方的list
# squares = []  # 创建一个空list赋值给squares
# for vaule in range(1, 11):  # 使vaule遍历数字1-10
#     square = vaule ** 2  # 把vaule平方赋值给squae
#     squares.append(square)  # 把变量square赋值给squares
# print(squares)  # 打印变量squares

# 简写方法-列表解析
squares = [vaule ** 2 for vaule in range(1, 11)]
print(squares)

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # 创建一个数字list
print(min(digits))  # 求出数字list中最小数
print(max(digits))  # 求出数字list中最大数
print(sum(digits))  # 求出数字list数字总和
