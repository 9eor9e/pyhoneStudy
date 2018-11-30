# 使用for循环来遍历list中的所有数据。

# 创建list，使用for循环遍历list中魔法师姓名。
# magicians = ['alice','mary','helan']
# print(magicians)
# for magician in magicians:
#     print(magician)


magicians_2 = ['alice','mary','helan']
for magician in magicians_2:
    print(magician + ',thanks for your trick!')
    print("I can't wait to see your next trick," + magician.title() + '\n')
print("Thank you,everyone.That was a great magic show!")