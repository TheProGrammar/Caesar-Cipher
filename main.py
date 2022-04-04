import string

# TODO:

letter_list = []
for i in range(26):
    letter_list.append(string.ascii_lowercase[i])
for i in range(26):
    letter_list.append(string.ascii_lowercase[i])

#print(letter_list)

print("""
                                             _         _                 
                                            (_)       | |                
  ___   __ _   ___  ___   __ _  _ __    ___  _  _ __  | |__    ___  _ __ 
 / __| / _` | / _ \/ __| / _` || '__|  / __|| || '_ \ | '_ \  / _ \| '__|
| (__ | (_| ||  __/\__ \| (_| || |    | (__ | || |_) || | | ||  __/| |   
 \___| \__,_| \___||___/ \__,_||_|     \___||_|| .__/ |_| |_| \___||_|   
                                               | |                       
                                               |_|                       
""")

type_choice = input("Do you want to encrypt or decrypt? Type 'e' or 'd': ")

user_word = input("Enter a word: ")
password_shift = int(input("Enter a shift amount: "))

encrypted_word = ""

if type_choice == "d":
    password_shift *= -1

for letter in user_word:
    letter_index = letter_list.index(letter)
    new_index = letter_index - password_shift
    encrypted_word += letter_list[new_index]

print(encrypted_word)