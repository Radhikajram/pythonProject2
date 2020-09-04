import time
import random
name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")

time.sleep(1)
print("start guessing")
time.sleep(0.5)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("Guess the characters")

guesses =  ''

turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print("you won")
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

    if turns == 0:
        print("You Loose")
