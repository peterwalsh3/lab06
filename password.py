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


def decode(encoded_password):
    decoded_password = ''
    for num in encoded_password:
        num = int(num)
        num_decoded = (num - 3) % 10
        decoded_password += str(num_decoded)
    return decoded_password
    


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
            decoded_password = decode(new_password)
            print(f"The encoded password is {new_password}, and the original is {decoded_password}.")
        elif option == 3:
            break


if __name__ == "__main__":
    main()
