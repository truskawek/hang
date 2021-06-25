import sys
import requests
import json
import random

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
jsonObj = response.json()
people = jsonObj["people"]
randomName = random.choice(people)["name"].rsplit(' ', 2)[0].lower()

word = randomName.lower()
user_word = []
used_letters = []
 
def find_indexes(word, letter):
    indexes = []
    
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes
 

for _ in word:
    user_word.append("_")
 
while True:
    try:
        no_of_tries = int(input("Enter number of tries: "))
        break
    except ValueError:
        print("Enter numeric value :)")
        
while True:
    
    letter = input("Enter a letter: ").lower()
    if not letter.isalpha():
        print("Enter a letter")
        continue
    if len(letter) != 1:
        print("Enter ONE letter")
        continue
    used_letters.append(letter)
    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print("There's no such letter in your word :(")
        no_of_tries -= 1
        print("Tries left: ", no_of_tries,)
        
        if no_of_tries == 0:
            print("It was nice...to meet you")
            sys.exit()
            
    else:
        for index in found_indexes:
            user_word[index] = letter
        whole_word = "".join(user_word)
        if whole_word == word:
            print("WOW, VICTORY!!! :D")
            sys.exit()
        print("".join(user_word))

    print("Used letters: ", used_letters )
        