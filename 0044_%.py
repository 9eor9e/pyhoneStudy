# %求模运算符 - 求余数示例
# print(4 % 3)
# print(5 % 3)
# print(6 % 3)
# print(7 % 3)

# 使用%求模运算符来判断even偶数和odd奇数 - 示例2
number = input("Enter a number, and I 'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")