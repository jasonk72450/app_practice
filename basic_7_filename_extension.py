# Basic 6
# Get filename from user and print the extension

filename = input("Input the Filename: ")
f_extens = filename.split(".")
print("The extension of the file is : " + repr(f_extens[-1]))
