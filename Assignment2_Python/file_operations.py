#write to a file
# file = open("justFile.txt", "w")

# file.write("Hello, this is my first Python file.\n")
# file.write("I am learning file handling in Python.")

# file.close()

# print("Content written to file successfully.")


# read from a file
file = open("justFile.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()