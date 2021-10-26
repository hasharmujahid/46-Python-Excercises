# Exercise 22 - Caesar's Cipher In cryptography, a Caesar cipher is a very simple encryption techniques in which each
# letter in the plain text is replaced by a letter some fixed number of positions down the alphabet. For example,
# with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar,
# who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar
# cipher where the shift is 13. In Python, the key for ROT-13 may be represented by means of the following dictionary:
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
directions = input("enter 'encode' to encrypt and 'decode' to decrypt ").lower()
shift_val = int(input('enter the shift value'))
text = str(input("enter the text "))


def encryption(plain_text, shift_value):
    cypher_text = ''
    for letters in plain_text:
        pos = alphabets.index(letters)
        new_pos = pos + shift_value
        cypher_text += alphabets[new_pos]
    print(f"your encrypted text is {cypher_text}")
    return cypher_text


def decrytion(encrypted_text, shiftval):
    decrypt = ''
    for letter in encrypted_text:
        pos = alphabets.index(letter)
        new_pos = pos - shiftval
        decrypt += alphabets[new_pos]
    print(f"your decrypted text is {decrypt}")


if directions == 'encode':
    encryption(text, shift_val)
if directions == 'decode':
    decrytion(encrypted_text=text, shiftval=shift_val)
