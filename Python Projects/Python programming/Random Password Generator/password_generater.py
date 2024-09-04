import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation

    password =''.join(random.choice(char) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter the desired length of password: "))

        if length <= 0:
            print("Please enter a positive integer for the length")
            return
        password = generate_password(length)

        print("Generate Password:",password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__=="__main__":
    main()  