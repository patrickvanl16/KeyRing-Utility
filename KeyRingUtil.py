# This file takes a username and password. Utilizes the KeyGen package to store it into the OS' credential store.
# More information with additional options, if you are interested:
# http://theautomatic.net/2020/04/28/how-to-hide-a-password-in-a-python-script/

import keyring

print("Welcome to a KeyRing password setter/getter. Please enter a following number: ")
print("[1] - New service")
print("[2] - Remove service")
choice = input("Please choose a number: ")
if choice == "1":
    serviceName = input("Service name: ")
    username = input("Username: ")
    password = input("Password: ")
    password2 = input("Verify password: ")

    if password == password2:
        keyring.set_password(serviceName, username, password)
        print("Done.")
    else:
        print("Passwords didn't match.")

if choice == "2":
    serviceName = input("Service to delete: ")
    username = input("Username associated with service: ")
    verify = input("Are you sure? This action cannot be undone. (Type Y or N): ")

    if verify == "Y":
        try:
            keyring.delete_password(serviceName, username)
            print("Done.")
        except:
            print("An error occurred. Are you sure you entered everything correctly and that the ring exists?")
    else:
        print("Service did not get removed.")