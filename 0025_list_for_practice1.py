# for循环练习1
# numbers = list(range(1,21)) # 创建包含1-20的list
# for number in numbers: # 把list中所有的数据赋值给number
#     print(number) # list中的数据，每赋值一个给number就打印一个

# 练习2
# numbers = list(range(1,1000001)) # 创建包含1-1000000的list
# for number in numbers: # 把list中所有的数据赋值给变量number
#     print(number) # list中的数据，每赋值一个给变量number就打印一个

# 练习3
# print(min(numbers)) # 打印出numbers list中最小的数据
# print(max(numbers)) # 打印出numbers list中最大的数据
# print(sum(numbers)) # 打印出numbers list中所有数据的和

# 练习4
# numbers = list(range(1,20,2)) # 创建一个包含1-20范围里的奇数list
# for number in numbers: # 把numbers list中的所有数据赋值给变量number
#     print(number) # 打印出变量number所有的值

# 练习5
# numbers = list(range(3,31)) # 创建一个包含3-30的数字的list
# for number in numbers: # 把numbers list中的所有数据赋值给变量number
#     if number%3 == 0: # 如果变量number的值除以3的余数等于0
#         print(number) # 打印出符合上面条件的变量number的值

# 练习6
cubeds = [] # 创建一个空list cubeds
for vaule in range(1,11): # 把1-10分别赋值给变量vaule
    cube = vaule ** 3 # 每被赋值一次的变量vaule再赋值给cube
    cubeds.append(cube) # 把被赋值的变量cube的值添加到cubes list中
print(cubeds) # 打印cubeds list数据

cubes = [vaule**3 for vaule in range(1,11)]
print(cubes)