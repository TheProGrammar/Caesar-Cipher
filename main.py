import string
from data import game_logo

# TODO:

letter_list = []
for i in range(26):
    letter_list.append(string.ascii_lowercase[i])

print(game_logo)

type_choice = input("Do you want to encrypt or decrypt a message? Type 'e' or 'd': ")

user_word = input("Enter a word: ")
password_shift = int(input("Enter a shift amount: "))

encrypted_word = ""

if type_choice == "d":
    password_shift *= -1

for letter in user_word:
    letter_index = letter_list.index(letter)
    new_index = letter_index - password_shift
    if new_index >= len(letter_list):
        new_index -= len(letter_list)
    encrypted_word += letter_list[new_index]

print(f"Your word is {encrypted_word}")
