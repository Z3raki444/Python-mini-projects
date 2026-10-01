alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) % 26  # Ensure shift is within alphabet range
def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift if direction == 'encode' else -shift
            new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            result += new_char
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result
if direction == 'encode':
    encoded_text = caesar_cipher(text, shift, 'encode')
    print(f"Encoded message: {encoded_text}")
elif direction == 'decode':
    decoded_text = caesar_cipher(text, shift, 'decode')
    print(f"Decoded message: {decoded_text}")
# If the user inputs 'encode', the program will encrypt the message.
# If the user inputs 'decode', the program will decrypt the message.
