print("Welcome to the number guessing game")
t = int(input("Upload the upper limit -->"))
import random
a = random.randint(0,t)
guess = 0
while True:
  print('Make a guess')
  guess += 1
  b = int(input())
  if b == a:
    print("You guessed it correct!")
    break
  elif b< a:
    print("You guessed smaller number")
  else:
    print("You guessed larger number")

print('You took', guess,'guesses to get it correct')