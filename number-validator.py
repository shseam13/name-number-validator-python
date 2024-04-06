def numberValidator():
    check = True
    user_number = "+88" + input("Enter 11 digit bd number(01xxxxxxxxx):")
    try:
        if user_number[2:]=="" or len(user_number)<14 or len(user_number)>14:
            print("Please enter number again.!")
            check=False
            exit(101)
        else:
            for number in user_number[1:]:
                if number in '!@#$%^&*)(=+-/\\<>,.?}{]["|:;~`':
                    print("Don't use any special character!")
                    check=False
                    exit()
        if user_number[5] not in "3456789":
            print("Only BD numbers allowed!")
            check=False
            exit()
        elif check==True:
            print(user_number + " is correct!")
    except IndexError:
        print("Number must be 11 digit!")

numberValidator()