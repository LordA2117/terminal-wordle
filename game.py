from termcolor import colored
import requests
import os
from time import sleep
import random
from pprint import pprint


def getLetterColors(word, original_word):
    coloredList = []
    for i in range(len(word)):
        if word[i] == original_word[i]:
            coloredList.append(colored(word[i], 'green'))

        if word[i] != original_word[i] and word[i] in original_word:
            coloredList.append(colored(word[i], 'yellow'))

        if word[i] != original_word[i] and word[i] not in original_word:
            coloredList.append(word[i])

    return ''.join(coloredList)

    # Instructions screen
print(colored('Wordle is a game where you guess a word which contains a given number of letters', 'cyan'))
print(('Legend: '))
print('1.', colored('green', 'green'),
      ': Signifies that the letter is in the word and in the correct position')
print('2.', colored('yellow', 'yellow'),
      ': Signifies that the letter is in the word but not in the correct position')
print('3. white : The letter is not in the word')
input()
os.system('cls')

api = 'https://random-word-api.herokuapp.com/'

print('Choose your difficulty: ')
print('1.', colored('Easy', 'green'), ': 3 letter word, 5 attempts')
print('2.', colored('Medium', 'yellow'), ': 5 letter word, 5 attempts')
print('3.', colored('Hard', 'red'), ': 8-10 letter word, 5 attempts')
difficulty = int(input('Enter the difficulty number(1, 2 or 3): '))

length = 0
if difficulty == 1:
    length = 3

elif difficulty == 2:
    length = 5

elif difficulty == 3:
    length = random.choice([8, 9, 10])

word_unformatted = requests.get(f"{api}word?length={length}").text
word = word_unformatted.replace('"', '')
word = word.replace('[', '')
word = word.replace(']', '')

columnLength = len(word)
rowLength = 6

# Code for the main wordle interface
i = 0
os.system('cls')
wordTable = ['-'*columnLength for i in range(rowLength)]
for row in wordTable:
    print(f'    {row}   ')

while i < 6:
    guess = input('Word: ')
    if guess.lower() == word:
        print(colored('You Win!!', 'cyan'))
        break

    if len(guess.lower()) != len(word):
        print(f'Word must be of length {len(word)} not {len(guess)}')
        i += 1
        continue

    if guess.lower() != word:
        coloredWord = getLetterColors(guess, word)

    wordTable[i] = coloredWord
    os.system('cls')
    for row in wordTable:
        print(f'    {row}   ')
    i += 1
else:
    print(colored(f'The word was {word}', 'magenta'))
