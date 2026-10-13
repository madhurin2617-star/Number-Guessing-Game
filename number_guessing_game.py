<<<<<<< HEAD

import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        print("Attempts:", attempts)
        break
=======

import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        print("Attempts:", attempts)
        break
>>>>>>> 3223722f8dd1761602b2ddb0a110f7a412f6fc64
