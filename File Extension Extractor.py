# Write a Python program that accepts a filename from the user and prints the extension of the file.

filename = input("input the filename: ")

f_extns = filename.split(".")

print("The extension of the file is : " + repr(f_extns[-1]))
