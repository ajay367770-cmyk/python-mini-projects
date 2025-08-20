import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
        break
