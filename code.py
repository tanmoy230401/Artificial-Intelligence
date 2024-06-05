
letters = 'abcdefghijklmnopqrstuvwxyz'
matters = 'mnopqrstuvwxyzabcdefghijkl'

num_letters = len(letters)

def encrypt(plaintext):
     ciphertext = ''
     for letter in plaintext:
         letter = letter.lower()
         if not letter == ' ':
           index = letters.find(letter)
           if index == -1:
                 ciphertext += letter
           else:
             new_index = index
             if new_index >=num_letters :
                 new_index -=num_letters
             ciphertext +=matters[new_index]
     return ciphertext


def decrypt(ciphertext):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index
                if new_index < 0:
                   new_index += num_letters
                plaintext += matters[new_index]
    return plaintext

print()
print('*** Monoalphabetic cipher program ***')
print()

print('Encrypt or Decrypt')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
     print('Encryption modem selected ')
     print()
     text = input('enter the text to encrypt : ')
     ciphertext=encrypt(text)
     print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('Decryption mode selected')
    print()
    text = input(' enter the text to decrypt : ')
    plaintext = decrypt(text)
    print(f'PLAINTEXT: {plaintext}')


