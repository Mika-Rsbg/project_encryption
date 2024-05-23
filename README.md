# Project Encryption

Welcome to the encryption_project GitHub repository! This repository contains Python code for various encryption methods. Currently, the Caesar cipher is fully implemented, while the Enigma, Public Key, and Vigenère ciphers are placeholders that will be completed in the future.

## Contents

- **Caesar Cipher**: Fully implemented Caesar cipher encryption algorithm.
- **Enigma Cipher**: Placeholder for the Enigma cipher.
- **Public Key Cipher**: Placeholder for the Public Key encryption.
- **Vigenère Cipher**: Placeholder for the Vigenère cipher.

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

The Caesar cipher is already implemented and can be used directly. The other encryption methods are currently placeholders.

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

## Placeholder Methods

The following methods are still in progress and currently serve as placeholders in the code:

- `enigma_cipher()`
- `public_key_cipher()`
- `vigenere_cipher()`

## Contributing

Contributions to this repository are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-encryption-method`).
3. Make your changes and commit them (`git commit -m 'Add new encryption method'`).
4. Push the branch (`git push origin feature/new-encryption-method`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please open an issue in the GitHub repository or contact me directly.

Happy encrypting!
