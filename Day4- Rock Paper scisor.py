import random
user_input=int(input("what do you choose? Type 0 for rocke, 1 for 1 for paper, 2 for scisossor"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
items=[rock,paper,scissors]
#print users choice
if user_input==0:
    print("you picked Rock")
    print(rock)
elif user_input==1:
    print("you picked Paper")
    print(paper)
elif user_input==2:
    print("you picked Scissor")
    print(scissors)
else:
    print("Invalid input")
computer_input= random.randint(0,2)
#print users choice
if computer_input==0:
    print("computer picked Rock")
    print(rock)
elif computer_input==1:
    print("computer picked Paper")
    print(paper)
elif computer_input==2:
    print("computer picked Scissor")
    print(scissors)
else:
    print("Invalid input")

#game logic
if user_input==(computer_input):
    print("Game drawn")
elif user_input==0 and computer_input==1:
    print("computer won")
elif user_input==1 and computer_input==2:
    print("You won")
elif user_input==2 and computer_input==0:
    print("You won")
elif user_input==0 and computer_input==2:
    print("computer won")
elif user_input==1 and computer_input==2:
    print("computer won")
elif user_input==2 and computer_input==1:
    print("you won")
