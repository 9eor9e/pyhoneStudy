# 使用remove方法删除list中数据

motocycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motocycles)

# 不知道数据位置，只要知道数据内容可以使用remove方法删除数据
motocycles.remove('ducati')
print(motocycles)

# remove方法删除数据练习2
# 被删除的数据可以再次使用，把删除的数据保存到新的变量中。
# 如果list中有重复的数据，remove方法只能删除重复数据中的第一个数据。
motocycles_2 = ['honda', 'yamaha', 'suzuki','ducati']
print(motocycles_2)

too_expensive = 'ducati'
motocycles_2.remove(too_expensive)
print(motocycles_2)
print('\nA '+ too_expensive + ' is too expensive for me!')