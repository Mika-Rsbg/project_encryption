# Project Encryption

Welcome to the encryption_project GitHub repository! This repository contains Python code for various encryption methods. Currently, the Caesar cipher is fully implemented, the Enigma cipher and decipher is in progress, while the Public Key, and Vigenère ciphers are placeholders that will be completed in the future.

## Contents

- **Caesar Cipher**: Fully implemented Caesar cipher encryption algorithm.
- **Enigma Cipher**: Parts of the Enigma Cipher were already added.
- **Public Key Cipher**: Placeholder for the Public Key encryption.
- **Vigenère Cipher**: Placeholder for the Vigenère cipher.
- **Decipher**: Mostly placeholders for the decipher methodes of the cipher methodes.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Mika-Rsbg/encryption_project.git
   cd encryption_project
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

The Caesar cipher is already implemented and can be used directly. The Enigma Cipher is practicly all ready added and should work, so you can use it directly. The other encryption methods are currently placeholders.

### Example: Caesar Cipher

The Caesar cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

#### Example Code

```python
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
                key += 1
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

# Example usage of the Caesar cipher
print(caesar_cipher("This is a test", 2))
```

### Placeholder Methods

The following methods are still in progress and currently serve as placeholders in the code:

- `public_key_cipher()`
- `vigenere_cipher()`
- `caesar_decipher()`
- `public_key_decipher()`
- `vigenere_decipher()`

### "In-Progress" Methodes

The following methods have been added partly and will be completly ready soon:

- `enigma_cipher()`
- `enigma_decipher()`

### Example: Enigma Cipher

The Enigma cipher is a complex encryption machine used by the Germans during World War II.

#### Example Code

```python
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
    
    ciphertext = "".join(ciphertext_letters)
    
    return ciphertext

print(enigma_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
```

### Decipher Methods

Decipher methods have been added to the project for decryption purposes.

#### Example Code

```python
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

print(enigma_decipher("efphpwlhmwlpw"))
```

## Contributing

Contributions to this repository are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-encryption-method`).
3. Make your changes and commit them (`git commit -m 'Add new encryption method'`).
4. Push the branch (`git push origin feature/new-encryption-method`).
5. Create a pull request.
   
## License

This project is licensed under the MIT License. See the <a href="/Mika-Rsbg/project_encryption/blob/main/LICENSE">LICENSE</a> file for details.

## Contact

If you have any questions or suggestions, please open an issue in the GitHub repository or contact me directly.

#### Happy encrypting!
