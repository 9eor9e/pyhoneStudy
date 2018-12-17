# dictionary字典中嵌入list列表 - 示例1
# alien_0 = {'colour':'green','point':'5'}
# alien_1 = {'colour':'yellow','point':'10'}
# alien_2 = {'colour':'red','point':'15'}
# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

# dictionary字典中嵌入list列表 - 示例2
# 使用range()来产生大量外星人
# aliens = [] # 建议一个空的外星人列表list
# for alien_number in range(30): # 使用for循环遍历30次并赋值给alien_number
#     new_alien = {'colour':'green','point':'5','speed':'slow'} # 在for循环下定义新外星人字典
#     aliens.append(new_alien) # 在for循环中把新定义的外星人添加到aliens列表list中
# for alien in aliens[:5]: # 使用for循环遍历aliens列表前5个外星人并赋值给alien变量
#     print(alien) # 在for循环中每遍历到一个外星人就打印一次
# print("...") # 打印...
# print("Total number of aliens: " + str(len(aliens))) # 打印Total number of aliens：和aliens列表长度并转换成字符串

# dictionary字典嵌入list列表 - 示例3
aliens = []
for alien_number in range(30):
    new_alien = {'colour':'green','point':'5','speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
for alien in aliens[:5]:
    print(alien)
print('...')
