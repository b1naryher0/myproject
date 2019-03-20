# Some code from the book Automate The Boring Stuff.
passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()

print("Enter your password.")
    typedPassword = input()

if typedPassword = secretPassword:
        print("Access granted")
        if typedPassword == "12345":
            print("Thats the password idiots put on their luggage.")
else:
    print("Access Denied.")            
