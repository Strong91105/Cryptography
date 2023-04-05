# Fernet 128-bit AES

from cryptography.fernet import Fernet

key = ""

def GenerateKey():
    key = Fernet.generate_key()

    print("Your key is: " + key.decode("utf-8"))
    print("CAUTION! The password cannot be decrypted if the key is misplaced")
    print("\n")
    main()

def encrypt(key):
    encrypter = Fernet(key)
    phrase = input("Enter Password: ")
    cipher = encrypter.encrypt(bytes(phrase, 'utf-8'))
    print(cipher)
    main()


def decrypt(key):
    encrypter = Fernet(key)
    phrase = input("Enter Encrypted Password: ")
    decryptString = encrypter.decrypt(phrase)
    print(decryptString.decode("utf-8"))
    main()




def main():
    print("1. Generate Key")
    print("2. Encrypt with Key")
    print("3. Decrypt with Key")

    nav_option = input()

    if nav_option in "1":
        print("\n")
        GenerateKey()

    elif nav_option in "2":
        print("\n")
        key = input("Enter key: ")
        encrypt(key)

    elif nav_option in "3":
        print("\n")
        key = input("Enter key: ")
        decrypt(key)

    else:
        print("Invalid selection")
        main()


main()