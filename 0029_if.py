# if条件判断语句
# cars = ['audi','bmw','toyota','sabaru']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# if条件判断所返回的值其实就是ture或者false
# ture就执行，false就不执行

# car = 'bmw'
# car == 'bmw'

# 使用in来判断需求的数据是否在list中
cars = ['audi','bmw','toyota','sabaru']
for car in cars:
    if 'bmw' in car:
        print('BMW in the cars!')
