# tuple元组，数据内容不可更改。

# dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])
#
# # 试图修改dimensions第一个数据
# # dimensions[0] = 250 # 系统会提示，元组数据不可更改。
#
# for dimension in dimensions:
#     print(dimension)

# 元组数据不可更改，但可以给元组变量重新赋值。
dimensions = (200,50)
print('Original dimensions : ')
print(dimensions)

dimensions = (250,100)
print('\nModified dimensions : ')
print(dimensions)