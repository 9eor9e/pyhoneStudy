# 在字典dictionary嵌入列表list - 示例2
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite languages is :")
    else:
        print("\n" + name.title() + "'s favorite languages are :")
    for language in languages:
        print("\t" + language.title())