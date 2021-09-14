import random
from password import Password

def main():
    print(Password.generatePassword())

if __name__ == "__main__":
    try:
        main()
    except:
        print("Error, Try to Came back later")
