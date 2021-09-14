import random

class Password:
    def __init__(self):
        pass

    @classmethod
    def generatePassword(cls):
        level = int(input("""
What is the Level of the Password:
Press 1 For Low
Press 2 For Medium
Press 3 For High
"""))
        if level == 1:

        length = int(input("Put the Length of the password that you need: "))
        special_chars_len = int(input("Put the Number of special chars you want in the Password: "))
        nums_len = int(input("Put the Number of numbers you want in the Password: "))
        alpha_chars_len = int(input("Put the Number of alphabet chars in the Password: "))

        chars = "ABCDEFGHIJKLMNOQRSTUVWXYZabcdefghijklmnoqrstuvwxyz"
        special_chars = "!@#$%^&*()_+\|/<>';~-=+_"
        nums = "0123456789"

        final_chars = ""

        for i in range(special_chars_len):
            my_char = special_chars[round(random.uniform(0, special_chars_len))]
            while my_char in final_chars:
                my_char = special_chars[round(random.uniform(0, special_chars_len))]
            final_chars += my_char

        for i in range(nums_len):
            my_char = nums[round(random.uniform(0, nums_len))]
            while my_char in final_chars:
                my_char = nums[round(random.uniform(0, nums_len))]
            final_chars += my_char

        for i in range(alpha_chars_len):
            my_char = chars[round(random.uniform(0, alpha_chars_len))]
            while my_char in final_chars:
                my_char = chars[round(random.uniform(0, alpha_chars_len))]
            final_chars += my_char

        print(final_chars)
        
        password = ""

        for i in range(length):
            my_char = final_chars[round(random.uniform(0, length - 1))]
            while my_char in password:
                my_char = final_chars[round(random.uniform(0, length - 1))]
            password += my_char

        return password

