def vigenere_cipher2(plaintext, key_word):
    plaintext_lower = plaintext.lower()
    plaintext_letters = list(plaintext_lower)
    letter_numbers = []

    ciphertext_letters = []

    ciphertext = ""
    for element in ciphertext_letters:
        ciphertext += element

    return ciphertext


def vigenere_cipher(plaintext, key_word):
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

    key_word_lower = key_word.lower()
    key_letters = list(key_word_lower)
    key_numbers = []

    for x in key_letters:
        key_numbers.append(ord(x) - ord('a') + 1)

    key_index = 0

    for a in letter_numbers:
        if isinstance(a, int):
            if a <= 26:
                b = (a - 1 + key_numbers[key_index % len(key_numbers)]) % 26 + 1
                ciphertext_letters.append(chr(b + ord('a') - 1))
                key_index += 1
            elif a <= 36:
                c = a - 27
                ciphertext_letters.append(str(c))
            elif a == 100:
                ciphertext_letters.append(" ")
        else:
            ciphertext_letters.append(a)

    ciphertext = "".join(ciphertext_letters)
    return ciphertext
