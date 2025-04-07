# Write a Python program that accepts a full name and prints the initials in uppercase.
def get_initials(name):
    # Split the name into words
    words = name.split()
    # Get the first letter of each word and convert to uppercase
    initials = ''.join(word[0].upper() for word in words)
    return initials

# Get user input
full_name = input("Enter your full name: ")
print(full_name)
# Print the initials
print("Initials:", get_initials(full_name))


