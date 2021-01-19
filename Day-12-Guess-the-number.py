import random


guess_list=list(range(1,101))
c_guess=random.choice(guess_list)
def hard():
    user_input=0
    i=5
    while user_input!=c_guess and i>0:
        user_input=int(input('enter your guess: '))
        def guess_again():
            if i>1:
                return 'Guess again'
            else:
               return  ""
        if user_input==c_guess:
            print('your guess is correct, You win')
            i -=1
            break
        elif user_input > c_guess:
            print('Too high\n {} \n you have {} attemps remaining to guess the number'.format(guess_again(),i-1))
            i += 1
        elif user_input < c_guess:
            print('Too low\n {} \n you have {} attemps remaining to guess the number'.format(guess_again(),i-1))
            i -= 1
        if user_input!=c_guess and i==5:
            print('you lost')

def easy():
    user_input=0
    i=10
    while user_input!=c_guess and i>0:
        user_input=int(input('enter your guess: '))
        def guess_again():
            if i>1:
                return 'Guess again'
            else:
                return ""
        if user_input==c_guess:
            print('your guess is correct, You win')
            i -=1
            break
        elif user_input > c_guess:
            print('Too high\n {} \n you have {} attemps remaining to guess the number'.format(guess_again(),i-1))
            i -= 1
        elif user_input < c_guess:
            print('Too low\n {} \n you have {} attemps remaining to guess the number'.format(guess_again(),i-1))
            i -= 1
        if user_input != c_guess and i==10:
            print('you lost')


again='y'
while again=='y':
    c_guess = random.choice(guess_list)
    difficulty = input('Choose a Difficulty, Type easy or hard:  \n').lower()
    if difficulty=='easy':
        easy()
        again=input('Do you want to play again??y/N'.lower())
    elif difficulty=='hard':
        hard()
    again = input('Do you want to play again??y/N'.lower())
print('you have ended the game')
