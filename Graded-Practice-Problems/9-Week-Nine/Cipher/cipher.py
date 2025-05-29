
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAMES:
# DATE:
# CLASS:
# Program Title: Cipher Puzzle
# To run: open the terminal, type python3 cipher.py
#
# Indicate here which Bonus Options were implemnted: 
#
############################################################################

# When you are ready to submit the completed code to Canvas...
# 👇👇 Copy and paste in your code from the notebook "cipher.ipynb" below 👇👇
# Download this .py file, and upload it to the associated Canvas assignment



def encrypt(alphabet, plain_text, key):
    alphabet_length = len(alphabet)
    text_length = len(plain_text)
    cipher_text = ""
    
    index = 0
    while index < text_length:
        if plain_text[index] != " ":
            letter_location = 0
            while letter_location < alphabet_length:  
                upper_case = plain_text[index].upper()
                if alphabet[letter_location] == upper_case:
                    cipher_letter_location = (letter_location + key) % alphabet_length
                    cipher_letter = alphabet[cipher_letter_location]
                    cipher_text = cipher_text + cipher_letter     
                letter_location = letter_location + 1
        else:
            cipher_text = cipher_text + " "
        index = index + 1

    return cipher_text


#-----WRITE THE DECRYPT FUNCTION HERE------










def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = 3
    message = input("Enter a message to encrypt (no punctuation marks or symbols): ")
    secret_message = encrypt(alphabet, message, key)
    print(f"Your encrypted message is: {secret_message}")

    #Use your decrypt function here to decipher the cipher text

main()