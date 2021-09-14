import random
import string

def main():
    level = int(input("""
Put the Level of Password You want
1 For Low
2 For Medium
3 For High
"""))
    print(generatePassword(level))


def generatePassword(level):
    if level == 1:
        length = 12

    elif level == 2:
        length = 18

    elif level == 3:
        length = 24

    else:
        raise Exception("Invalid Input")

    chars = string.ascii_letters
    special_chars = string.punctuation
    nums = string.digits

    chars_len = len(chars) - 1
    special_len = len(special_chars) - 1
    nums_len = len(nums) - 1

    char_length = length // 3

    final_chars = ""

    for i in range(char_length):
        my_char = special_chars[round(random.uniform(0, special_len))]
        while my_char in final_chars:
            my_char = special_chars[round(random.uniform(0, special_len))]
        final_chars += my_char

    for i in range(char_length):
        my_char = nums[round(random.uniform(0, nums_len))]
        while my_char in final_chars:
            my_char = nums[round(random.uniform(0, nums_len))]
        final_chars += my_char

    for i in range(char_length):
        my_char = chars[round(random.uniform(0, chars_len - 1))]
        while my_char in final_chars:
            my_char = nums[round(random.uniform(0, chars_len - 1))]
        final_chars += my_char
        
    password = ""

    for i in range(length):
        my_char = final_chars[round(random.uniform(0, length - 1))]
        while my_char in password:
            my_char = final_chars[round(random.uniform(0, length - 1))]
        password += my_char

    return password


if __name__ == "__main__":
    main()

