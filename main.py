# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def menu():
    password = ""
    encoded_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        try:
            option = int(input("Please enter an option: "))
        except:
            print("Not a valid option!")
            menu()

        match option:
            case 1:
                try:
                    password = int(input("\nPlease enter your password to encode: "))
                except:
                    print("Not a valid option!")
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            case 2:
                print(f"The encoded password is {encoded_password}, and the original password is {decode(password)}.")
            case 3:
                break
            case _:
                print("Not a valid option!")

def encode(password):
    stringify = ""
    for number in str(password):
        match number:
            case "0":
                stringify += "3"
            case "1":
                stringify += "4"
            case "2":
                stringify += "5"
            case "3":
                stringify += "6"
            case "4":
                stringify += "7"
            case "5":
                stringify += "8"
            case "6":
                stringify += "9"
            case "7":
                stringify += "0"
            case "8":
                stringify += "1"
            case "9":
                stringify += "2"
            case _:
                pass
    return int(stringify)

def decode(password):
    return password

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

