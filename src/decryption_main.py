def caesar_decipher(cipertext, key):
    ciphertext_lower = cipertext.lower()
    ciphertext_letters = list(ciphertext_lower)
    letter_numbers = []
    control_chars = ['.', ',', '!', '?', '"', ':', ';', '(', ')']

    for letter in ciphertext_letters:
        if letter.isalpha():
            letter_numbers.append(ord(letter) - ord('a') + 1)
        if letter.isdigit():
            x = int(letter) + 27
            letter_numbers.append(x)
        if letter == " ":
            letter_numbers.append(100)
        if letter in control_chars:
            letter_numbers.append(letter)
    
    plaintext_letters = []

    for number in letter_numbers:
        if isinstance(number, int):
            if number <= 26:
                number -= key
                number = (number - 1) % 26 + 1
                plaintext_letters.append(chr(number + ord('a') - 1))
            elif number <= 36:
                plaintext_letters.append(str(number - 27))
            elif number == 100:
                plaintext_letters.append(" ")
        else:
            plaintext_letters.append(number)

    plaintext = "".join(plaintext_letters)
    return plaintext
        

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

def public_key_decipher():
    pass
def vigenere_decipher():
    pass

print(enigma_decipher("efphpwlhmwlpw"))
print(caesar_decipher('dxc wdi hdfv mjnziwzmbzm piy dxc wdi vh  25.05.2010 bzwjmzi. yvn dno zdi wzdnkdzg ozso! "cvggj", nvboz gdnv.', 73))