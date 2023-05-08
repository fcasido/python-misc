def caesar_cipher(ciphertext, shift):
    """
    Decode a message that has been encrypted using a Caesar cipher with a specified shift value.
    The shift value determines the number of positions to shift each letter in the message.
    """
    result = ""

    # Iterate through each letter in the ciphertext
    for letter in ciphertext:
        # Determine the ASCII code for the current letter
        char_code = ord(letter)

        # Shift the ASCII code back by the specified number of positions
        if letter.isalpha():
            char_code = (char_code - 65 - shift) % 26 + 65

        # Convert the new ASCII code back to a character and append it to the result string
        result += chr(char_code)

    return result

# Example usage
ciphertext = "WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ"
right_shift = 3
decrypted_message = caesar_cipher(ciphertext, right_shift)
print("Decrypted message:", decrypted_message)

#The decrypted message is:
#
#THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
