### Part Two -- your code goes here. 
import random

x = random.randint (1,100)

guessed = False
while guessed == False:
  guess = int(input("Try to guess a number from 1 to 100: "))
  if guess == x:
    guessed = True
    print("You guessed correctly")
  else:
    print("Unlucky, that wasn't the correct number. Try again. ")