# peter walsh
def encode(password):
    encoded_password = ''
    for num in password:
        num = int(num)
        if 0 <= num <= 6:
            encoded_password += str(num + 3)
        else:
            encoded_password += str(num - 7)
    return encoded_password


def decode(password):
    pass


def main():
    while True:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            orig_password = input('Please enter your password to encode: ')
            new_password = encode(orig_password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            pass
        elif option == 3:
            break


if __name__ == "__main__":
    main()
