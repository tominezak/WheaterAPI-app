import random
import string

chars = ' ' + string.punctuation + string.digits + string.ascii_letters  # Combining punctuation, digits, and letters
chars = list(chars)  # Convert the string to a list for random selection
key = chars.copy()

random.shuffle(key)  # Shuffle the key list to create a random key

# ENCRYPTION
plain_text = input("Enter the text to encrypt: ")
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)  # Find the index of the letter in the chars list
    cipher_text += key[index]  # Append the corresponding character from the shuffled key

print(f'Plain text: {plain_text}')
print(f'Encrypted text: {cipher_text}')

# DECRYPTION
cipher_text = input("Enter the text to decrypt: ")
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)  # Find the index of the letter in the chars list
    plain_text += chars[index]  # Append the corresponding character from the shuffled key

print(f'Encrypted text: {cipher_text}')  
print(f'Plain text: {plain_text}')
