def decrypt(cipher, key = 12):
    plain_text = ""
    for num in cipher:
        plain_text += chr(int(num / (key*311)))
    return plain_text

def dynamic_xor_encrypt(semicipher, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(semicipher):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text[::-1]


if __name__ == "__main__":
    cipher = [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]
    text_key = "trudeau"
    semi_cipher = decrypt(cipher, 12)
    plain_text_dynamic = dynamic_xor_encrypt(semi_cipher, text_key)
    print(plain_text_dynamic)
