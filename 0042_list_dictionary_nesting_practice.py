# list和dictionary嵌套练习 - 1
# pipi = {
#     'teddy':'JieZhao'
# }
# chongwu2 = {
#     'xishi':'ZhaoYingYing'
# }
# pets = [pipi,chongwu2]
# for pet in pets:
#     print(pet)

# list和dictionary嵌套练习 - 2
# favorote_places = {
#     'luyong':['bali','thailand','chongqing'],
#     'luxinyu':['hongkong','japaness'],
#     'zhaoyingying':['chengdu','hongkong','thailand'],
# }
# for name,place in favorote_places.items():
#     print("\n" + name.title() + "'s favorite places are : " )
#     for places in place:
#         print(places.title())

# list和dictionary嵌套练习 - 3
cities = {
    'shanghai':{
        'country':'china',
        'population':'20000000',
        'fact':'moderm',
    },
    'tokyo':{
        'country':'japan',
        'population':'16000000',
        'fact':'fashion',
    },
    'taibei':{
        'country':'taiwan',
        'population':'12000000',
        'fact':'hot',
    },
}
for city,infoes in cities.items():
    print("\n" + city.title())
    country_info = "Country: " + infoes['country'] + "\n" + "Population: " + infoes['population'] + "\n" + "Fact : " + infoes['fact']
    print(country_info)