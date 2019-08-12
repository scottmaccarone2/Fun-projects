# The goal of this file is to create a random number guessing game.
# If the guess is too high, the output will say so; if the guess is
# too low, the output will say so.

# To make this more random, find a way for the range of values that the
# random number is selected from to also be random!

import random
p1 = random.randint(1, 100)
p2 = random.randint(1, 100)
if p1 > p2:
    my_num = random.randint(p2, p1)
    print("I am thinking of a number between " + str(p2) + " and " + str(p1) + ".")
    print("What is your guess?")
elif p1 < p2:
    my_num = random.randint(p1, p2)
    print("I am thinking of a number between " + str(p1) + " and " + str(p2) + ".")
    print("What is your guess?")

# Use some kind of loop in case the user repeatedly enters invalid inputs
try:
    guess = int(input())
except ValueError:
    print("Oops! You entered a non-numeric value! Try again:")
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
