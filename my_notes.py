# Write three notes to a new file
with open("my_notes.txt", "w") as f:
    f.write("Python is fun\n")
    f.write("Files are useful\n")
    f.write("Week 7 is about file handling\n")
    

# Add a fourth note WITHOUT erasing the first three
with open("my_notes.txt", "a") as f:
    f.write("I added this later\n")

# Read the file back and print each line with no blank lines between
print("--- My notes ---")
with open("my_notes.txt", "r") as f:
    for line in f:
        # Print the line without its newline character
        print(line.strip())
# Count the lines
with open("my_notes.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))