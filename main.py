import sys 


def encrypt(message, k):
    encrypted_message = ""
    for x in message.lower():
        if x.isalpha(): # Check if the character is an alphabet letter
            # If the character is lowercase, set shift to ord('a') - 97; if it's uppercase, set shift to ord('A') - 65
            shift = ord('A') if x.isupper() else ord('a')  
             # Encrypt the character using a Caesar cipher, transforming the letter into a secret code (number) and then back to a letter
            encrypted_x = chr((ord(x) - shift + k) % 26 + shift) 
            encrypted_message += encrypted_x
        else:
            encrypted_message += x
    return encrypted_message


def decrypt(message, k):
    return encrypt(message, -k)


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypt_message = encrypt(message, key)

    # decrypt your encrypted word
    decrypted_message = decrypt(encrypt_message, key)

    print("Your encrypted word is", encrypt_message)
    print("Your decrypted word is", decrypted_message)


