menu = {'espresso' : '$3.00', 'americano' : '$3.00', 'macchiato' : '$3.50' , 'cortado' : '$4.00' , 'cappuccino' : '$4.00' , 'pour-over' : '$5.00' , \
    'iced brew' : '$4.00' , 'iced tea' : '$3.00' , 'milk tea' : '$5.00' , 'cupp joe' : '$5.00' , 'chai latte' : '???' , 'matcha latte' : '???' , 'hot cocoa' : '???'}
food = ''
size = ''
size2 = ''
print(menu)
food = input('Please type in the name of the food(all lower case, and make sure you spell it right!)')
chai = {'8oz' : '$3.75' , '12oz' : '$4.00' , '16oz' : '$4.25'}
cocoa = {'8oz' : '$3.00' , '12oz' : '$3.25' , '16oz' : '$3.50'}
if food == 'chai latte' or 'matcha latte':
    size = input('What size do you want?(8oz, 12oz, 16oz)')
    print(chai.get(size))
elif food == 'hot cocoa':
    size2 = input('What size do you want?(8oz, 12oz, 16oz)')
    print(cocoa.get(size2))
else:
    print(menu.get(food))
