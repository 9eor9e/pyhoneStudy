# 使用for循环遍历字典键 - 值对
# 其中使用了两个变量key和vaule来赋值
# user_0 = {
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }
# for key,vaule in user_0.items():
#     print('\nKey : ' + key)
#     print('Vaule : ' + vaule)

# 可以使用简单命名变量来实现
# 其中.item()是dictionart的方法
# user_0 = {
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }
# for k,v in user_0.items():
#     print('\nKey : ' + k)
#     print('Vaule : ' + v)

# 使用for循环遍历dictionary示例2
# 这个示例中，用来存储遍历字典的两个变量使用了name和language，这样命名方式清楚直接明了。
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# 使用for循环遍历字典的键，keys()方法的使用示例
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# # for name in favorite_languages.keys():
# # 遍历字典时会默认遍历所有的键，所以如果不使用keys()方法，效果相同。
# for name in favorite_languages:
#     print(name.title())

# 遍历字典，并对相应的姓名打印特殊消息示例
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() +
#               ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")

# 遍历字典，方法keys()不但可以遍历字典所有键，还能用于检查某个变量是否在其中
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# if 'erin' not in favorite_languages.keys():
#     print("Erin,please take our poll!")

# 使用函数sorted()，按顺序遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ",thank you for taking the poll.")

# 使用for遍历字典时，使用vaules()方法来遍历所有的值。
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# for循环遍历字典所有值后，使用set()来使得到的值使独一无二的。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned :")
for language in set(favorite_languages.values()):
    print(language.title())
