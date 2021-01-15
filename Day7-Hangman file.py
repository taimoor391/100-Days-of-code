import hangman_art as art
import hangman_list_of_words as wrd
import random

print(art.logo)

chosen_word =list(random.choice(wrd.word_list))

guess_word=[]
for i in range(0,len(chosen_word)):
  guess_word.append("_")
print(guess_word)

tries=6
while tries>0 and "_" in guess_word:
  guess = input("Guess a letter: ").lower()
  if guess in guess_word:
      print("you have already entered this letter, try another letter")
  for a,letter in enumerate(chosen_word):
        if letter == guess:
          guess_word[a]= letter
        else:
           pass
  print(guess_word)
  print(art.stages[tries])

  if guess not in chosen_word:
    print("the letter {} you guessed is not in a word,please try again".format(guess))
    tries=tries-1
    print("you have {} tries left".format(tries) )
if tries> 0 and   "_"  not in guess_word:
  print("you win")
else:
  print(" you lost")