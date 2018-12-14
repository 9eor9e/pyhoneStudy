# dirtionary字典的使用方法
# 存储的数据以键 - 值对的形式，可以存储包括数值、list(列表)、dictionary(字典)
# alien_0 = {'colour':'green','points':'5'}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# 一开始可以创建一个空字典，然后再把需要的键 - 值对添加进去
# 使用字典来存储用户提供的数据或在编写能自动生成大量键 - 值对的代码时，通常都需要先定义一个空字典。
# alien_0 = {}
# alien_0['colour'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# 修改字典中的值
# alien_0 = {'colour':'green'}
# print("The alien is " + alien_0['colour'] + ".")
# alien_0['colour'] = 'yellow'
# print("The alien is now "+ alien_0['colour'] + ".")

# 删除字典键 - 值对,使用del语句+字典名称+键，被删除的键 - 值对永久消失了。
# alien_0 = {'colour':'green','point':'5'}
# print(alien_0)
# del alien_0['point']
# print(alien_0)

# 内容较多的字典格式示例和过长print语句格式示例。
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")