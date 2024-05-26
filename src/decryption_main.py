def caesar_decipher():
    pass

def enigma_decipher(ciphertext):
    ciphertext_lower = ciphertext.lower()
    ciphertext_letters = list(ciphertext_lower)
    letter_numbers = []

    addition = [[5, 'f'], [-2, 'z'], [4, 'g'], [1, 'e'], [7, 'l'], [-7, 'y'], [-3, 'd'],
                [2, 'j'], [-1, 'h'], [4, 'n'], [-2, 'i'], [-1, 'k'], [2, 'o'], [-1, 'm'],
                [3, 'r'], [1, 'q'], [2, 's'], [6, 'x'], [-3, 'p'], [3, 'w'], [1, 'v'],
                [7, 'c'], [-3, 't'], [3, 'a'], [3, 'b'], [-5, 'u']]

    # Create a dictionary to map each letter to its corresponding number
    letter_to_number = {item[1]: item[0] for item in addition}

    for letter in ciphertext_letters:
        if letter.isalpha():
            # Find the original number using the ciphertext letter
            original_number = letter_to_number[letter]
            # Calculate the shift value based on the original and the encrypted letter
            shift_value = original_number
            decrypted_number = (ord(letter) - ord('a') + 1 - shift_value) % 26
            if decrypted_number == 0:
                decrypted_number = 26
            letter_numbers.append(decrypted_number)

    decrypted_letters = []

    for number in letter_numbers:
        if number <= 26:
            decrypted_ascii = number + ord('a') - 1
            decrypted_letters.append(chr(decrypted_ascii))
    
    plaintext = "".join(decrypted_letters)
    
    return plaintext


ciphertext = "efphpwlhmwlpw"
plaintext = enigma_decipher(ciphertext)
print("Der entschlüsselte Text ist:", plaintext)

def public_key_decipher():
    pass
def vigenere_decipher():
    pass