def is_valid_password(password):
    if len(password) < 6:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*" for c in password):
        return False
    return True


# Input password from user and validate
password = input("Enter a strong password (min 6 chars, upper, lower, digit, special char): ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Please try again.")
    exit()  # Stop program if invalid


# Save the valid password to a file
with open("password_store.txt", "w") as file:
    file.write(password)


# Password check loop for file access
while True:
    user = input("Enter the password to access the file: ")
    with open("password_store.txt", "r") as file:
        content = file.read()
    
    if content == user:
        print("Access granted!")
        break  # Exit the loop on successful access
    else:
        print("Incorrect passw
