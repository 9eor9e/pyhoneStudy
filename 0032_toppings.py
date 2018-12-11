# for_if_elif_elso练习

# requested_toppings = ['mushrooms','greenpeppers','extra cheese']
# for requested_topping in requested_toppings:
#     print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")

# 如果添加的某样材料用完了的情况
# requested_toppings = ['mushrooms', 'greenpeppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'greenpeppers':
#         print("Sorry,we are out of greenpeppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")

# 如果pizza浇头list是空的，返回让客户确认信息。
# 在python中list如果是空，if判断会返回false值。
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_toppings + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plainpizza?")