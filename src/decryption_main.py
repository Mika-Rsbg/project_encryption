def caesar_decipher():
    pass

def enigma_decipher(ciphertext):
    ciphertext_lower = ciphertext.lower()
    ciphertext_letters = list(ciphertext_lower)
    letter_numbers = []

    addition = [['a', 5], ['b', -2], ['c', 4], ['d', 1], ['e', 7], ['f', -7], ['g', -3], 
                ['h', 2], ['i', -1], ['j', 4], ['k', -2], ['l', -1], ['m', 2], ['n', -1], 
                ['o', 3], ['p', 1], ['q', 2], ['r', 6], ['s', -3], ['t', 3], ['u', 1], 
                ['v', 7], ['w', -3], ['x', 3], ['y', 3], ['z', -5]]

    for x in ciphertext_letters:
        for item in addition:
            if x == item[0]:
                # Umgekehrte Verschiebung: von der verschlüsselten Position zur Ausgangsposition
                y = (ord(x) - ord('a') - item[1]) % 26
                if y == 0:
                    y = 26
                letter_numbers.append(y)

    plaintext_letters = []

    for a in letter_numbers:
        if a <= 26:
            b = a
            plaintext_letters.append(chr(b + ord('a') - 1))

    # Rückgabe des entschlüsselten Texts als Zeichenkette
    return ''.join(plaintext_letters)

# Test
ciphertext = "FgPQK"
decrypted_text = enigma_decipher(ciphertext)
print("Entschlüsselter Text:", decrypted_text)

def public_key_decipher():
    pass
def vigenere_decipher():
    pass