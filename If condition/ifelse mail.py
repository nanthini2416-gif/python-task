username = input("Enter your username: ")
email = input("Enter your email ID: ")

if username:
    print("Username is valid")
else:
    print("Invalid username")

if "@" in email and "." in email:
    print("Email ID is valid")
else:
    print("Invalid email ID")
