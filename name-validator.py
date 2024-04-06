def checkNameValidation():
    check = True
    user_name = input("Enter name: ")
    if user_name=="":
        print("Please enter name!")
    else:
        for name in user_name:
            if name in "0123456789":
                print("Can't use numbers in name.")
                check=False
                exit(101)
            elif name in '+-~`!@#$%^&*()_<>?,./\\{[}|"]':
                print("Special characters are not allowed.")
                check=False
                exit()
            elif name in "'":
                print("Special characters are not allowed")
                exit()
    if check:
        print("Valide name!")

checkNameValidation()