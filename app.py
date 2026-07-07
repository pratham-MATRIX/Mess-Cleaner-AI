"""
MessCleaner

Version : v0.1.0

Author : Pratham Singh Thakur

Description:
MessCleaner is an open-source Python project that aims to simplify file
management through automation.

The current release provides a command-line interface for basic file
operations. Future updates will introduce intelligent file organization,
AI-assisted search, automation, duplicate detection, and a modern graphical
user interface.

Status:
Active Development
"""

import os

# Create a new file if it doesn't already exist
def create_file():
    filename = input("Enter filename: ")
    try:
        with open(filename, "x") as file:
            print(f"{filename} created successfully!\n")
    except FileExistsError:
        print(f"{filename} already exists.\n")
    except Exception as e:
        print(f"Some error occurred...  {e}\n")

# Display all files and directories in the current working directory
def view_all_files():
    files = os.listdir()
    
    if not files:
        print("No files found...\n")
    else:
        for file in files:
            if os.path.isdir(file):
                print(f"{file}/")
            else:
                print(file)

# Remove an existing file
def delete_file():
    filename = input("Enter filename: ")
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!\n")
    except FileNotFoundError:
        print(f"{filename} not found.\n")
    except Exception as e:
        print(f"Some error occurred...  {e}\n")

# Read and display file contents
def read_file_content():
    filename = input("Enter filename: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            if content=="":
                print(f"{filename} is empty.\n")
            else:
                print(f"Content of {filename}-->\n{content}\n")
    except FileNotFoundError:
        print(f"{filename} not found.\n")
    except Exception as e:
        print(f"Some error occurred...  {e}\n")

# Append new text to an existing file
def append_to_file():
    filename = input("Enter filename: ")
    try:
        with open(filename,"a+") as file:
            content = input("Enter content to append: ")
            print(f"Appending content to {filename}...\n")
            file.write(content + "\n")
            print(f"Content appended successfully!\n")
    except FileNotFoundError:
        print(f"{filename} not found.\n")
    except Exception as e:
        print(f"Some error occurred...  {e}\n")


while True:
    print("\n\t------Welcome to the File Manager!------\t")
    print("""
1. Create a file
2. View all files
3. Delete a file
4. Read file content
5. Edit file content
6. Exit

""")

    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        create_file()
    elif choice == "2":
        view_all_files()
    elif choice == "3":
        delete_file()
    elif choice == "4":
        read_file_content()
    elif choice == "5":
        append_to_file()
    elif choice == "6":
        print("Exiting...")
        
        break
    else:
        print("Invalid choice. Please try again.\n")