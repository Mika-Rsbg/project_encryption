def caesar_cipher(plaintext, key):
    plaintext_lower = plaintext.lower()
    plaintext_letters = list(plaintext_lower)
    letter_numbers = []
    control_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    control_chars = ['.', ',', '!', '?', '"', ':', ';', '(', ')']

    for x in plaintext_letters:
        if x == " ":
            letter_numbers.append(100)
            continue
        if x in control_numbers:
            letter_numbers.append(int(x) + 27)
            continue
        if x in control_chars:
            letter_numbers.append(x)
            continue
        letter_numbers.append(ord(x) - ord('a') + 1)

    ciphertext_letters = []

    for a in letter_numbers:
        if isinstance(a, int):
            if a <= 26:
                b = (a - 1 + key) % 26 + 1
                ciphertext_letters.append(chr(b + ord('a') - 1))
            elif a <= 36:
                c = a - 27
                ciphertext_letters.append(str(c))
            elif a == 100:
                ciphertext_letters.append(" ")
        else:
            ciphertext_letters.append(a)

    ciphertext = ""
    for element in ciphertext_letters:
        ciphertext += element

    return ciphertext

def enigma_cipher(plaintext):
    plaintext_lower = plaintext.lower()
    plaintext_letters = list(plaintext_lower)
    letter_numbers = []

    addition = [['a', 5], ['b', -2], ['c', 4], ['d', 1], ['e', 7], ['f', -7], ['g', -3], 
            ['h', 2], ['i', -1], ['j', 4], ['k', -2], ['l', -1], ['m', 2], ['n', -1], 
            ['o', 3], ['p', 1], ['q', 2], ['r', 6], ['s', -3], ['t', 3], ['u', 1], 
            ['v', 7], ['w', -3], ['x', 3], ['y', 3], ['z', -5]]

    for x in plaintext_letters:
        for item in addition:
            if x == item[0]:
                y = (ord(x) - ord('a') + 1 + item[1]) % 26
                if y == 0:
                    y = 26
                letter_numbers.append(y)

    ciphertext_letters = []

    for a in letter_numbers:
        if a <= 26:
            b = a
            ciphertext_letters.append(chr(b + ord('a') - 1))

    ciphertext = ""
    for element in ciphertext_letters:
        ciphertext += element
    
    return ciphertext
        
def public_key_cipher():
    pass

def vigenere_cipher(plaintext, key_word):
    plaintext_lower = plaintext.lower()
    plaintext_letters = list(plaintext_lower)
    key_word_lower = key_word.lower()
    key_word_letters = list(key_word_lower)
    letter_numbers = []

    key_length = len(key_word_letters)
    key_indices = [ord(letter) - ord('a') for letter in key_word_letters]

    for i, letter in enumerate(plaintext_letters):
        if letter.isalpha():
            x = ord(letter) - ord('a')
            y = key_indices[i % key_length]  # Use the index to repeat the key
            z = (x + y) % 26
            if z == 0:
                z = 26
            letter_numbers.append(z)
        else:
            letter_numbers.append(letter)

    ciphertext_letters = []

    for number in letter_numbers:
        if isinstance(number, int):
            if number < 0:
                print("warning: error")
            cipher_letter = chr(number + ord('a'))
            ciphertext_letters.append(cipher_letter)
            if number <= 0:
                print("warning: error")
                print(cipher_letter)
        else:
            ciphertext_letters.append(number)
            print(number)

    print(plaintext_letters)
    print(letter_numbers)
    print(ciphertext_letters)


print(caesar_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2))
print(caesar_cipher('Ich bin Mika Rosenberger und ich bin am  25.05.2010 geboren. Das ist ein beispiel Text! "Hallo", sagte Lisa.', 73))
print(enigma_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
vigenere_cipher("abcdefghijklmnopqrstuvwxyz", "w")