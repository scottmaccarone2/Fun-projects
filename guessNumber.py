# The goal of this file is to create a random number guessing game.
# If the guess is too high, the output will say so; if the guess is
# too low, the output will say so.

import random
my_num = random.randint(1,25)

print("I am thinking of a number between 1 and 25.")
print("What is your guess?")

# Consider exception handling if the user inputs, say a letter instead of a
# number; or some other symbol other than a positive number
guess = int(input())

if guess == my_num:
    print("Great job! You guessed my number on the first try!")

num_attempts = 1
while guess != my_num:
    if guess > my_num:
        num_attempts += 1
        print("Your guess is too high. Try again:")
        guess = int(input())
        continue
    elif guess < my_num:
        num_attempts += 1
        print("Your guess is too low. Try again:")
        guess = int(input())
        continue

print("Great job! You guessed my number in " + str(num_attempts) + " guesses")
