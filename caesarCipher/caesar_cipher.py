#!/usr/bin/env python3

text_space = "abcdefghijklmnopqrstuvwxyz"

plain_text = input("Enter message, for example HELLO: ").lower()
shift = int(input("Enter shift, for example 6: "))
 
length = len(plain_text)
cipher_text = ""

for index in range(length):
    letter = plain_text[index]
    init_pos = text_space.find(letter)
    if init_pos < 0:
       cipher_text += " "
    else:
        letter_shift = (init_pos + shift) % 26
        cipher_text += text_space[letter_shift]
        
print("Cipher text: ", cipher_text)

