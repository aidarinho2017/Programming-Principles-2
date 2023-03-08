filename = input("Enter the file name: ")

with open(filename, 'r') as file:
    num_lines = sum(1 for line in file)

print("Number of lines in the file:", num_lines)