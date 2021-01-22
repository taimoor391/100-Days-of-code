import Day15Data as data



 # coffee function here

#coffee function here Save coffe requirement here

def process_coins(x):
    """input the coffee cost"""
    print('please pay $ {}'.format(x))
    print('inster coins\n')
    quarters = int(input('How many quarters?    '))
    dimes = int(input('How many dimes?    '))
    nickle = int(input('How many nickle?    '))
    pennies = int(input('How many pennies?    '))
    paid = 0.25 * quarters + 0.10 * dimes + 0.05 * nickle + 0.01 * pennies
    print(paid)
    net = paid - x
    if net < 0:
        print('Sorry thats not enough money. Money refunded{}'.format(paid))
        return False

    else:
        print('Thanks you paid {}, {} is returned\nEnjoy your coffee'.format(paid, net))
        return True


def resource_check(resources,order):
    for i in resources:
        if resources[i] < order[i]:
            print('sorry not enough {}'.format(i))
            return False

    else:
        return True

def report(resources):
    for i in resources:
        print("current status {}:  {}".format(i,resources[i]))

reset='no'

while reset=='no':
    user_input = input('What would you like? (espresso/latte/cappuccino):?').lower()
    resources = data.resources
    #print(resources)
    if user_input == 'report':
        report(resources)
    else:
        order = data.MENU[user_input]['ingredients']
        coffe_cost = data.MENU[user_input]['cost']

        if (resource_check(resources, order)):
            if process_coins(coffe_cost) :
                for i in resources:
                    resources[i] = resources[i] - order[i]
            else:
                pass
            #print(process_coins(coffe_cost))

    #reset=input("Do you want to reset the machine? yes or no:   ").lower()







#calculate current inventory
def current_inventory(x):
    """input coins function to determine if the transaction went through"""
    if process_coins(x):
        water=data.resources['water']-data.MENU[user_input]['cost']
        milk=data.resources['milk']-data.MENU[user_input]['cost']
        coffee=data.resources['coffee']-data.MENU[user_input]['cost']
        return water,milk,milk,coffee
    else:
        water = data.resources['water']
        milk = data.resources['milk']
        coffee = data.resources['coffee']
        return water, milk, milk, coffee

