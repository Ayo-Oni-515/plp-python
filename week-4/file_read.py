# program reads and writes to a new file
file_content = ""

with open("file.txt", "r") as file:
    file_content = file.read()


with open("new_file.txt", "w") as new_file:
    new_file.write(file_content)
