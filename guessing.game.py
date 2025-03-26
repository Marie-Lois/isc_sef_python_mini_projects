import random

number_to_guess = random.randint(1, 100)
attempts = 0

while True:  #Execute the code while it is true
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulation! You found the number in {}attempts" .format(attempts))