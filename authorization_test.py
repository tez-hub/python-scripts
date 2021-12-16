print("AUTHENTICATION")
print("********************************************************************")

print("Please enter your name and password!")
print("********************************************************************")

print("Enter name:")

name = input("")
if name == 'username':
    print("Enter password:")
    password = input("")

    if password == 'password':
        print("ACCESS GRANTED")
        print("You are welcome again " + name)
    else:
        print("ACCESS DENIED")
        print("ENTER THE CORRECT CREDENTIALS")

else:
    print("CHECK YOUR USERNAME AND TRY AGAIN")