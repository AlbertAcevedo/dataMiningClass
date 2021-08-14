#!/usr/bin/env python3

text_space = "abcdefghijklmnopqrstuvwxyz"

cipher_text = input("Enter cipher text: ").lower()
shift = int(input("Enter shift, for example 6: "))
 
length = len(cipher_text)
plain_text = ""

for index in range(length):
    letter = cipher_text[index]
    init_pos = text_space.find(letter)
    if init_pos < 0:
       plain_text += " "
    else:
        letter_shift = (init_pos - shift) % 26
        plain_text += text_space[letter_shift]
        
print("Plain text: ", plain_text)

