# list列表中嵌入dictionary字典示例 - 1
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)