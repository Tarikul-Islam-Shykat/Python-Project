

import random

def guess(x):
    random_number = random.randint(1,x) # from 1 to range 'x'
    guess = 0
    while guess!= random_number:

        # checking for valid input
        while True:
            try:
                inp = int( input(f'Guess a number between 1 an {x} : '))
                if(inp < 0):
                    print("Negative cant be accepted.")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue
            else:
                guess = inp
                break

        if guess<random_number:
            print('Sorry, guess again. Too low')

        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f'Yay, congrats. You have guessed the the number {random_number} correctly ')



# checking for valid input
while True:
    try:
        range = int(input("Please enter the range : "))
        if(range<0):
            print("Please enter a positive number")
            continue
    except ValueError:
        print("Please enter a valid number")
        continue
    else:
        guess(range)
