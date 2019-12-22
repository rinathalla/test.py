import random

print('Hello........May I know your name')
Name = input()

print('Well,' + Name + ',I am thinking of a number between 1 to 20...Can you guess the numbr?')
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print('Take a Guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good Job ' + Name + ' You guessed it right')
else:
    print('Sorry you could not guess it right.The number was ' + str(guessTaken))
