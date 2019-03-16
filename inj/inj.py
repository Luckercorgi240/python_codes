menu = {'espresso' : 3.00, 'americano' : 3.00, 'macchiato' : 3.50 , 'cortado' : 4.00 , 'cappuccino' : 4.00 , 'pour-over' :  5.00 , \
    'iced brew' : 4.00 , 'iced tea' :  3.00 , 'milk tea' :  5.00 , 'cupp joe' :  5.00 , 'chai latte' : {'8oz':  3.00, '12oz':  3.75, '16oz': 4.25} , \
    'matcha latte' : {'8oz': 3.00, '12oz': 3.75, '16oz': 4.25} , 'hot cocoa' : {'8oz' : 3.00, '12oz' :  3.50, '16oz' : 4.25}}
for m in menu.keys():
    print(m)
# x = input('What do you want to order ')
# if x == 'chai latte':
#     size = input('What size do you want? (8oz, 12oz, 16oz)   ')
#     print(menu.get(x).get(size))
# else:
#     print(menu.get(x))
def order_drinks():
    more = True
    total = []
    while more == True:
        drink = input('What drink do you want?  ')
        if drink == 'chai latte' or drink == 'matcha latte':
            size = input('What size do you want?(8oz, 12oz, 16oz) ')
            print(menu.get('chai latte').get(size))
            if menu.get('chai latte').get(size) == None:
                pass
            else:
                total.append(menu.get('chai latte').get(size))
        elif drink == 'hot cocoa':
            size = input('What size do you want?(8oz, 12oz, 16oz)  ')
            print(menu.get('hot cocoa').get(size))
            if menu.get('hot cocoa').get(size) == None:
                pass
            else:
                total.append(menu.get('hot cocoa').get(size))
        else:
            print('The price for %s is %s' %(drink, menu.get(drink)))
            if menu.get(drink) == None:
                pass
            else:
                total.append(menu.get(drink))
        w = input('Do you want more?  ')
        if w == 'Yes' or w == 'yes':
            pass
        elif w == 'No' or w == 'no':
            more = False
            total = sum(total)
            print('Your total price is $%.2f' % total)
        else:
            print('I dont understand')
order_drinks()