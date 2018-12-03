# list切片方法

# numbers = list(range(1,7))
#
# print(numbers[:4]) # 打印numbers list第一位到第四位的数据
# print(numbers[2:]) # 打印numbers list第三位到最后位的数据
# print(numbers[1:5]) # 打印numbers list第二位到第五位的数据

# list切片方法来做list副本

my_favorite_pizza = ['bangerking','pisence','1dull']
friend_pizza = my_favorite_pizza[:]
my_favorite_pizza.append('aabbaa')
friend_pizza.append('ccddcc')
print(my_favorite_pizza)
print(friend_pizza )
for pizza in my_favorite_pizza:
    print('My favorite pizza are : ' + pizza.title() + '.')
for pizza2 in friend_pizza:
    print('My friend favorite pizza are : ' + pizza2.title() + '.')
