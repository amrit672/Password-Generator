import string # Importing string module to use its properties for getting letters, digits and punctuations
import random # Importing random module to use its functions for making a random password everytime

if __name__ == "__main__":
    sl = string.ascii_letters # Getting lowercase and uppercase letters
    sd = string.digits # Getting digits
    sp = string.punctuation # Getting punctuations

    # Adding all characters in a single list
    chs = []
    chs.extend(list(sl))
    chs.extend(list(sd))
    chs.extend(list(sp))

    passLen = 0

    # Taking length of password input from user
    while(True):
        try:
            passLen = int(input("Enter the password length you want: "))
            if(passLen >=0):
                break
            else:
                print("Invalid length entered\nTry Again")
        except ValueError:
            print("Invalid length entered\nTry Again")
        except Exception:
            print("Could not set password length")

    # Generating a random password of the given length
    password = "".join(random.choices(chs, k=passLen)) # k is the number of random elements picked from the list chs
    print(f"Your password is: {password}")

    choice = ""
    while(True):
        choice = input("Do you want to write your password in passwords.txt file [y/n]: ")
        choice.lower()
        # Writing password in a file
        if(choice == "y"):
            purpose = input("Purpose of this password: ")
            with open("passwords.txt", "a") as f:
                f.write(f"Purpose: {purpose}\nPassword: {password}\n\n")
            break
        elif(choice == "n"):
            break