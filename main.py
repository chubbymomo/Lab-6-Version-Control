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
                    continue
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            case 2:
                if password != "":
                    print(
                        f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.") # before the decode function was called on password, which decoded the original password, not the encoded version.
                else:
                    print("No password!")
                    continue
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
    return stringify # before it was int(stringify) which removed the zeroes at the beginning of the password


def decode(password):
    password_decoded_list = []
    password = str(password)
    for i in range(len(password)):
        if int(password[i]) < 3:
            match password[i]:
                case '0':
                    password_decoded_list.append('7')
                case '1':
                    password_decoded_list.append('8')
                case '2':
                    password_decoded_list.append('9')
        else:
            password_decoded_list.append(str(int(password[i])-3))
    password = ''.join(password_decoded_list)
    return password


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()