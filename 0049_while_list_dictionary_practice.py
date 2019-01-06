# 7-8 - 练习1
sandwich_orders = ['sw1','sw2','sw3']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print('I made your tuna sandwich ' + finished_sandwich.title() + ' .')
    finished_sandwiches.append(finished_sandwich)
print('\n--All finished sandwiches--')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-9 - 练习2