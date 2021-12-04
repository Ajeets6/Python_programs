import string


alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"


def decrypt():

    encrypted_message = input().strip().lower()
    print()
    key = 6

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    # print(decrypted_message)
    string = decrypted_message
    vowels = "AaEeIiOoUu"

    def Check_Vow(string, vowels):
        final = [each for each in string if each in vowels]
        print(len(final))
    # print(final)
    Check_Vow(string, vowels)


for _ in range(int(input())):
    decrypt()
