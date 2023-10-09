import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
#GENERATE LIST USING KEY
def rutor(key, new_chars):
    x = 0
    for i in new_chars:
        chars_index = new_chars.index(i)
        if x % 2 == 0:
            chars_index = 32 - new_chars.index(i)
        new_chars[chars_index], new_chars[int(key[x])] = new_chars[int(key[x])], new_chars[chars_index]
        x += 1
        if len(key) <= x:
            x = 0



#ENCRYPT
def encryption():
    new_chars = chars.copy()
    plain_text = input('Write your text to encrypt: ')
    key = input('Write your key (numbers only): ')
    cipher_text = ''
    rutor(key, new_chars)
    #rutor() #double shuffling
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += new_chars[index]

    print(cipher_text)

#DECRYPT
def decryption():
    new_chars = chars.copy()
    cipher_text = input('Write your encrypted text: ')
    key = input('Write a key to decrypt (numbers only): ')
    rutor(key, new_chars)
    plain_text = ''
    for letter in cipher_text:
        index = new_chars.index(letter)
        plain_text += chars[index]
    
    print(plain_text)

if __name__ == "__main__":
    while True:
        action = input('What do you want to do: (enc, dec, exit): ')
        if action == 'enc':
            encryption()
        elif action == 'dec':
            decryption()
        elif action == 'exit':
            break
        else:
            print('Invalid command, try again')