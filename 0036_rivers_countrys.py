# dictionary字典练习1 - 1
# rivers_countrys = {
#     'huanghe':'china',
#     'heliu2':'weizhi2',
#     'nile':'egypt',
# }
# for river,country in rivers_countrys.items():
#     print("The " + river.title() + " runs through " + country.title() + "." )

# dictionary字典练习1 - 2 - 打印出字典中的河流名称
# rivers_countrys = {
#     'huanghe':'china',
#     'heliu2':'weizhi2',
#     'nile':'egypt',
# }
# for rivers in rivers_countrys.keys():
#     print(rivers.title())

# dictionary字典练习1 - 3 - 打印出字典中的国家名称
rivers_countrys = {
    'huanghe':'china',
    'heliu2':'weizhi2',
    'nile':'egypt',
}
for country in rivers_countrys.values():
    print(country.title())