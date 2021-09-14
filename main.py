import random

hash_password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOQRSTUVWXYZ!@#$%^&*()_+][''\|;:?/><1234567890=-+_"

hash_length = len(hash_password)

def generatePassword(hash_length, hash_password):
    password = ""

    password_length = int(input("Put the Length of the Password: "))

    for i in range(password_length):
        password += hash_password[round(random.uniform(0, hash_length))]

    return password

print(generatePassword(hash_length, hash_password))

