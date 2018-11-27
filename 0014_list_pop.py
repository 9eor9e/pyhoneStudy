# 使用pop()方法删除list中数据，删除的数据还能使用。栈的概念。

motocycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motocycles)
# 默认被pop的是list中最后一个数据
popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)

# 使用pop()方法删除list数据练习2
motocycles_2 = ['honda', 'yamaha', 'suzuki','ducati']
print(motocycles_2)
# 可以使用pop()加上索引弹出指定位置数据
popped_first_motocycle = motocycles_2.pop(0)
print(motocycles_2)
print(popped_first_motocycle)