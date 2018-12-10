# if ...else...语句格式。
# 两个条件判断，只要通过判断一个，就执行其下缩进的代码块，另一个直接跳过。

# cars = ['subaru', 'bmw','toyota']
# if 'vw' in cars:
#     print('bmw is good car !')
# else:
#     print('I sorry!')

# 多个条件判断可以使用if...elif...else
# 但这种结构也有缺点，那就是一旦通过一个判断条件，就会跳过其它的判断语句。
age = 66
if age < 4:
    print('price:0')
elif age <= 18:
    print('price:10')
elif age <= 65:
    print('price:10')
else:
    print('price:5')