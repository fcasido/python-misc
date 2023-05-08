# Using vigenere cipher, this program will decrypt a ciphertext using a key and an alphabet
# To use this function, simply pass in the ciphertext, key, and alphabet as arguments.

def vigenere_decrypt(ciphertext, key, alphabet):
    plaintext = ''
    print(key, alphabet)
    
    key_index = 0
    for c in ciphertext:
        if c in alphabet:
            c_index = alphabet.index(c)
            k_index = alphabet.index(key[key_index])
            p_index = (c_index - k_index) % len(alphabet)
            plaintext += alphabet[p_index]
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += c
    return plaintext

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'secretkey'
ciphertext = 'llkjmlkxckxovwlkkc'
plaintext = vigenere_decrypt(ciphertext, key, alphabet)
print(plaintext)  # outputs: "thisisatestmessage"
