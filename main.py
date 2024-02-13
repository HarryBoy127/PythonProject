shift  = 10

message = "helloworld"
encrypted_message = ""

for  x in message:

    # check if character is uppercase letter:
     if x.isupper():

        # find the position in 0-25
        x_unicode = ord(x)

        x_index = ord(x) - ord("A")

        # we need a negative value on the shift
        x_index = (x_index + shift) % 26 

        # make a new character

        new_unicode =  x_index + ord("A")

        new_character = chr( new_unicode)

        # append to encrypt word
        encrypted_message += new_character

     else:
        # if the character is not lower case we should the letter as it is
        encrypted_message += x

shift  = 10

message = "rovvy gybvn"
decrypted_message = ""

for  x in message:

    # check if character is uppercase letter:
     if x.isupper():

        # find the position in 0-25
        x_unicode = ord(x)

        x_index = ord(x) - ord("A")

        # we need a negative value on the shift
        x_index = (x_index - shift) % 26 

        # make a new character

        new_unicode =  x_index + ord("A")

        new_character = chr( new_unicode)

        # append to decrypt word
        decrypted_message += new_character

     else:
        # if the character is not lower case we should the letter as it is
        decrypted_message += x
    

print("Your encrypted word is ",encrypted_message)
print("Your Decrypted word is ",decrypted_message)





    
