import hashlib

print("DICTIONARY ATTACK SIMULATOR")

# password to crack (for demonstration)
target_password = "admin123"

# hash the password
hashed_password = hashlib.sha256(target_password.encode()).hexdigest()

print("Target hash:", hashed_password)
print("Starting dictionary attack...\n")

# open dictionary file
with open("passwords.txt", "r") as file:

    for word in file:
        word = word.strip()

        # hash dictionary word
        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        print("Trying:", word)

        if hashed_word == hashed_password:
            print("\nPassword Found:", word)
            break
    else:
        print("Password not found in dictionary.")
