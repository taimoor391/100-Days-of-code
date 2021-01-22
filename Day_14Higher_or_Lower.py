import Day14Data as dat
import random
import Day14art as art
data=dat.data

#print(data)

def choice():
   return random.choice(data)

def brandprint(A)  :
    return ( (  ("{}, a {} from {}".format((A['name']), (A['description']),A['country'] ))))

def results_compare(A,B):
    if A['follower_count']>B['follower_count']:
        return 'a'
    else:
        return 'b'

branda=choice()
brandb=choice()
print(art.logo)
print('compare A {}'.format(brandprint(branda)))
print(art.vs)
print('\nAgaints B {}'.format(brandprint(brandb)))



player_choice=input("who has more follower A or B\n").lower()
score=0

while player_choice==results_compare(branda,brandb):
    score += 1
    print('you are right: current score: {}'.format(score))
    branda = choice()
    brandb = choice()
    print('compare A {}'.format(brandprint(branda)))
    print(art.vs)
    print('\nAgaints B {}'.format(brandprint(brandb)))
    player_choice = input("who has more follower A or B\n").lower()

print(" You are wrong Game ended , your final score: {} ".format(score))





