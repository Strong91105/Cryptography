# Vignère Cipher

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(phrase, key):
    encrypted = ""

    # Changing length of key to fit text
    split_phrase = [
        phrase[i: i + len(key)] for i in range(0, len(phrase), len(key))
    ]

    for each_split in split_phrase:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1
    print("Ciphertext: " + encrypted)
    main()
    return encrypted




    pass

def decrypt(cipher, key):
    # Changing length of key to fit text
    decrypted = ""
    split_encrypted = [
        cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1
    print("Plaintext: " + decrypted)
    main()



    pass

def main():
    print("\n" "1. Encrypt Phrase")
    print("2. Decrypt Cipher")

    nav_option = input()

    if nav_option in "1":
        key = ""
        print("\n")
        phrase = input("Enter Phrase: ")
        key = input("Enter Key: ")
        encrypt(phrase, key)

    elif nav_option in "2":
        key = ""
        print("\n")
        cipher = input("Enter Cipher: ")
        key = input("Enter Key: ")
        encrypt(cipher, key)
        decrypt()

    else:
        print("Invalid selection")
        main()

    pass

main()