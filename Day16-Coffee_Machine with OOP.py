from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=menu()


i=0
while i==0:
    order= input('What would you llike: {}'.format(menu.get_items()))
    if order=='report':
        print(money_machine.report())
        print(coffe_maker.report)
    elif order=='off':
        i=1
    else:
        drink=menu.find_drink(order)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(MenuItem.cost):
            coffe_maker.make_coffee(drink)