"""
Password Manager Program
"""
import random
import string

"""
Pseudo:

import module random



def main
    get string
    check if valid password
    print string
"""

VALID_CHAR = string.printable.strip()

# Password lengths
# Generate random password length
password_length = random.randint(8, 20)

# Minimum and Maximum length
MIN_LENGTH = 8
MAX_LENGTH = 20


def main():
    """Main password program"""
    # password = input(">>> ")
    # print(password)
    password = input(">>> ")
    while not valid_password(password):
        print('Invalid password')
        password = input(">>> ")
    print(password)


def valid_password(password):
    """Check if password is valid"""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        # Check if password has certain characters
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        else:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
        return False
    return True


main()
# valid_password()
