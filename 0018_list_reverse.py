# 使用reverse()方法打印list

cars = ['bmw','audi','toyota','subaru']
print(cars)
# reverse()方法是改变原排列顺序为倒过来排列，并且是永久性的。
cars.reverse()
print(cars)
# 如果要把顺序还原，只需对list再次使用reverse()方法
cars.reverse()
print(cars)