import sys 


def encrypt(message, k):
    encrypted_message = ""
    for x in message.lower():
        if x.isalpha():
            shift = ord('A') if x.isupper() else ord('a')
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


