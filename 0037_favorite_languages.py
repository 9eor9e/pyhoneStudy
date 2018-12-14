# dictionary字典练习2 - 1
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
peoples = ['jen','sarah','phil','bone','dora']
for people in peoples:
    if people in favorite_languages.keys():
        print(people + " , thank you very much!")
    else:
        print(people + " , Please take our poll!")