# Caesar Cipher



def encryption():
    password = input("Enter Phrase: ")
    shift = int(input("Enter Shift: "))

    encrypted_pword = ""

    def encrypt_password(password, shift):
        encrypted_pword = ""

        for i in range(len(password)):
            pword = password[i]

            # Accounting for spaces
            if pword == "":
                encrypted_pword += " "

            # Uppercase
            elif pword.isupper():
                encrypted_pword += chr((ord(pword) + shift - 65) % 26 + 65)

            else:
                encrypted_pword += chr((ord(pword) + shift - 97) % 26 + 97)

        return encrypted_pword

    print("Phrase: " + password)
    print("Encrpyted Phrase: " + encrypt_password(password, shift))
    print("\n" * 2)
    print("---------------------------------------------------------")

    navigate()



def decryption():
    password = input("Enter Phrase: ")
    shift2 = int(input("Enter Shift: "))
    shift = -1 * shift2

    encrypted_pword = ""

    def encrypt_password(password, shift):
        encrypted_pword = ""

        for i in range(len(password)):
            pword = password[i]

            # Accounting for spaces
            if pword == "":
                encrypted_pword += " "

            # Uppercase
            elif pword.isupper():
                encrypted_pword += chr((ord(pword) + shift - 65) % 26 + 65)

            else:
                encrypted_pword += chr((ord(pword) + shift - 97) % 26 + 97)

        return encrypted_pword

    print("Phrase: " + password)
    print("Encrpyted Phrase: " + encrypt_password(password, shift))
    print("\n" * 2)
    print("---------------------------------------------------------")

    navigate()

def brute_force():
    def brute_decrypt(password, shift):
        result = ""

        for char in password:
            decrypted_char = chr(ord(char) - shift)

            result += decrypted_char

        return result

    password = input("Enter Encypted Phrase: ")

    for shift in range (1, 26):
        result = brute_decrypt(password, shift)
        print(f"Shift {shift}: {result}")

    navigate()

def navigate():

    print("1. Encrypt a Phrase")
    print("2. Decrypt a Phrase")
    print("3. Brute Force Phrase")
    nav_option = input()

    if nav_option in "1":
        encryption()

    elif nav_option in "2":
        decryption()

    elif nav_option in "3":
        brute_force()

    else:
        print("Invalid selection")
        navigate()

navigate()