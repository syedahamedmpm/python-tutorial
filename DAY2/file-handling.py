# Write to a file

with open("output.txt", "w") as f:
    f.write('Hello, World!')



# Reading from a file
with open("output.txt", "r") as f:
    print(f.read())