import hashlib
import random
import string

# variable for max size of password
max_size = 0

def generate_password():
    return ''.join(random.choices(string.ascii_lowercase, k=max_size)) # generate a random password

def hashed_password():
    file = open("hashed_passwords.txt", "r")
    contents = file.readlines() # put the different lines in a list
    count = 0

    while True:
        password = generate_password()
        count = count + 1 # increment count
        hashedPass = hashlib.sha256(password.encode()).hexdigest() # generate a hash of the password
        for line in contents: # loop through the whole file line by line
            reading = line.split()
            if reading[1] == hashedPass:
                print("\nPassword cracked with " + str(count) + " number of different passwords tried.")
                print("Username: " + reading[0])
                print("Password: " + password)
                print("Hash: " + hashedPass)
                file.close()
                exit(1)

def salted_password():
    file = open("salted_passwords.txt", "r")
    contents = file.readlines()
    count = 0

    # instead of picking the first line, this picks a random line (password) to crack
    lines = 0
    for line in contents:
        lines = lines + 1
    random_number = random.randint(1, lines)

    fields = contents[random_number].split()
    salt = fields[1] # obtain the salt in the txt file
    username = fields[0]
    hash = fields[2]

    while True:
        password = generate_password()
        count = count + 1 # increment count
        hashedPass = hashlib.sha256((password + salt).encode()).hexdigest() # generate a hash of the password
        if hash == hashedPass:
            print("\nPassword cracked with " + str(count) + " number of different passwords tried.")
            print("Username: " + username)
            print("Salt: " + salt)
            print("Password: " + password)
            print("Hash: " + hashedPass)
            file.close()
            exit(1)

# Main program
while True:

    # get the max size of password and convert to an int
    max_size = int(input("\nChoose the max password size: "))

    print("\nChoose either the 2nd or 3rd password file to crack:")
    print("1. Hashed Password")
    print("2. Salted Password")
    print("3. Quit")
    choice = input("Select an option: ")

    if choice == "1":
        hashed_password()
    elif choice == "2":
        salted_password()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")