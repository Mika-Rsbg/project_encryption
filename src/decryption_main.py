def caesar_decipher():
    pass

def enigma_decipher(ciphertext):
    ciphertext_lower = ciphertext.lower()
    ciphertext_letters = list(ciphertext_lower)
    letter_numbers = []

    addition = [['a', 5, 'f'], ['b', -2, 'z'], ['c', 4, 'g'], ['d', 1, 'e'], ['e', 7, 'l'], ['f', -7, 'y'], ['g', -3, 'd'], 
                ['h', 2, 'j'], ['i', -1, 'h'], ['j', 4, 'n'], ['k', -2, 'i'], ['l', -1, 'k'], ['m', 2, 'o'], ['n', -1, 'm'], 
                ['o', 3, 'r'], ['p', 1, 'q'], ['q', 2, 's'], ['r', 6, 'x'], ['s', -3, 'p'], ['t', 3, 'w'], ['u', 1, 'v'], 
                ['v', 7, 'c'], ['w', -3, 't'], ['x', 3, 'a'], ['y', 3, 'b'], ['z', -5, 'u']]

    # Create a dictionary to map each letter to its third element value
    third_element_dict = {item[2]: item[0] for item in addition}

    for x in ciphertext_letters:
        if x.isalpha():
            # Find the original letter using the third element
            original_letter = third_element_dict[x]
            # Calculate the shift value based on the original and the encrypted letter
            shift_value = ord(x) - ord(original_letter)
            y = (ord(x) - ord('a') + 1 - shift_value) % 26
            if y == 0:
                y = 26
            letter_numbers.append(y)

    plaintext_letters = []

    for a in letter_numbers:
        if a <= 26:
            b = a
            plaintext_letters.append(chr(b + ord('a') - 1))
    
    plaintext = ""
    for element in plaintext_letters:
        plaintext += element
    
    return plaintext

# Beispiel für die Verwendung der Funktion
ciphertext = "fzgelydjhnikomrqsxpwvctabu"
plaintext = enigma_decipher(ciphertext)
print("Der entschlüsselte Text ist:", plaintext)

def public_key_decipher():
    pass
def vigenere_decipher():
    pass