# File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write("This is the first line.\n")
        file.write("Here is the second line with a number: 42\n")
        file.write("And the third line, including another number: 3.14\n")
except IOError as e:
    print(f"An error occurred while creating the file: {e}")
finally:
    print("File creation attempt completed.")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        contents = file.read()
        print("File contents:")
        print(contents)
except FileNotFoundError:
    print("The file does not exist.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File reading attempt completed.")

# File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("This is the fourth line, appended.\n")
        file.write("Here's the fifth line, also appended.\n")
        file.write("And the sixth line, continuing to append.\n")
except IOError as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    print("File appending attempt completed.")
