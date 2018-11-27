# list使用sort()方法对数据进行排列

# 创建list，并打印
cars = ['bmw','audi','toyota','subaru']
print(cars)
# 对list按字母顺序进行排列，这个排列是永久性的。
cars.sort()
print(cars)

# 对list按反字母顺序进行排列，这个排列是永久性的。
# 对一个使用过sort方法的list不能再对其使用sort。
cars_2 = ['bmw','audi','toyota','subaru']
cars_2.sort(reverse=True)
print(cars_2)

# 使用sorted()方法对list进行临时排列。
cars_3 = ['bmw','audi','toyota','subaru']
print('\nHere is the original list:')
print(cars_3)

print('Here is the sorted list:')
print(sorted(cars_3))

print('Here is the original list again:')
print(cars_3)