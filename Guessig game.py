# Wind-chill Temperature
# U64412214
# Name: Hyelampa Thlala Kolo
'''This program is intended to generate a random number and have the user guess that number correctly to win. The program also counts
   the amount of times the user has guesses. The user only have 10 guess then the game is over'''
import random

num = random.randint(1, 101)
print(num)
user_in = float(input('Enter a number between 1 and 100(inclusive):'))
attempts = 1


while attempts != 11:
    if num == user_in:
        print(f'You guessed it right!! You got it in {attempts} guesses!')
        break
    if attempts >= 10:
        print(f'Sorry, the number was {num}')
        break
    if user_in > 100:
        user_in = float(input('Very funny. Enter a number between 1 and 100 (inclusive):'))
    elif user_in < 0:
        user_in = float(input('Really? Enter another guess:'))
    elif user_in < num:
        user_in = float(input('Too low. Enter another guess:'))
        attempts += 1
    elif user_in > num:
        user_in = float(input('Too high. Enter another guess:'))
        attempts += 1
    else:
        print(f'You guessed it right!! You got it in {attempts} guesses!')





