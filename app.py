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
import shutil

categories = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp",
        ".svg", ".tif", ".tiff", ".ico", ".heic", ".heif",
        ".raw", ".cr2", ".nef", ".arw", ".dng"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv",
        ".webm", ".m4v", ".mpeg", ".mpg", ".3gp", ".ts",
        ".mts", ".m2ts", ".vob"
    ],

    "Music": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma",
        ".m4a", ".opus", ".aiff", ".alac", ".mid", ".midi"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt",
        ".tex", ".md", ".pages", ".epub", ".mobi"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".xlsm", ".csv", ".ods", ".tsv"
    ],

    "Presentations": [
        ".ppt", ".pptx", ".pptm", ".odp", ".key"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2",
        ".xz", ".cab", ".tgz", ".z", ".jar"
    ],

    "Applications": [
        ".exe", ".msi", ".app", ".apk", ".deb", ".rpm"
    ],

    "Libraries": [
        ".dll", ".so", ".dylib", ".lib", ".a"
    ],

    "Code": [
        ".py", ".pyw", ".ipynb",
        ".js", ".ts", ".jsx", ".tsx",
        ".java", ".c", ".cpp", ".h", ".hpp", ".cs",
        ".go", ".rs", ".php", ".rb", ".swift",
        ".kt", ".kts", ".dart", ".r", ".lua", ".pl",
        ".html", ".htm", ".css", ".scss", ".sass", ".less",
        ".sql", ".json", ".xml", ".yaml", ".yml", ".toml",
        ".ini", ".cfg", ".conf",
        ".sh", ".bash", ".zsh", ".fish",
        ".ps1", ".bat", ".cmd", ".vbs"
    ],

    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot"
    ],

    "Data": [
        ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb",
        ".parquet", ".feather", ".pkl", ".pickle",
        ".h5", ".hdf5", ".jsonl", ".ndjson"
    ],

    "Subtitles": [
        ".srt", ".ass", ".ssa", ".sub", ".vtt"
    ],

    "3D Models": [
        ".obj", ".fbx", ".stl", ".blend", ".3ds",
        ".dae", ".gltf", ".glb", ".3mf", ".max",
        ".ma", ".mb"
    ],

    "CAD": [
        ".dwg", ".dxf", ".iges", ".igs", ".step", ".stp"
    ],

    "Design": [
        ".psd", ".ai", ".eps", ".indd", ".xd",
        ".sketch", ".fig"
    ],

    "Disk Images": [
        ".iso", ".img", ".dmg", ".vhd", ".vhdx", ".vmdk"
    ],

    "Log Files": [
        ".log"
    ]
}

# Create a new file if it doesn't already exist
def create_file():
    file_name = input("Enter filename: ")
    file_ext = input("Enter file extension: ")
    file = file_name+"."+file_ext
    try:
        with open(file, "x") as file:
            print(f"{file} created successfully!\n")
    except FileExistsError:
        print(f"{file_name} already exists.\n")
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

# Organize files into category-wise folders
def organize_files():
    folder = input("Enter folder path to organize: ")

    if not os.path.exists(folder):
        print("Folder not found.\n")
        return

    if not os.path.isdir(folder):
        print("The given path is not a folder.\n")
        return

    organized_files = []
    files = os.listdir(folder)

    for file in files:
        file_path = os.path.join(folder, file)

        if not os.path.isfile(file_path):
            continue

        file_extension = os.path.splitext(file)[1].lower()
        category = None

        for category_name, extensions in categories.items():
            if file_extension in extensions:
                category = category_name
                break

        if category is None:
            category = "Others"

        category_path = os.path.join(folder, category)
        destination = os.path.join(category_path, file)

        if os.path.exists(destination):
            name, extension = os.path.splitext(file)
            count = 1

            while os.path.exists(destination):
                new_file = f"{name}_{count}{extension}"
                destination = os.path.join(category_path, new_file)
                count += 1

        organized_files.append(
            (file, category, file_path, destination)
        )

    if not organized_files:
        print("No files to organize.\n")
        return

    print("\nFiles to be organized:\n")

    for file, category, file_path, destination in organized_files:
        destination_name = os.path.basename(destination)
        print(f"{file:<20} → {category}/{destination_name}")

    while True:
        confirmation = input("\nContinue? (y/n): ").lower().strip()

        if confirmation == "y":
            break
        elif confirmation == "n":
            print("\nOrganization cancelled.\n")
            return
        else:
            print("Invalid choice. Please enter y or n.")

    print("\nOrganizing files...\n")

    for file, category, file_path, destination in organized_files:
        try:
            category_path = os.path.dirname(destination)
            os.makedirs(category_path, exist_ok=True)

            shutil.move(file_path, destination)

            destination_name = os.path.basename(destination)
            print(f"{file} → {category}/{destination_name}")

        except Exception as e:
            print(f"Could not move {file}: {e}")

    print("\nOrganization completed.\n")

# Display basic statistics of a folder
def folder_statistics():
    folder = input("Enter folder path: ")

    if not os.path.exists(folder):
        print("Folder not found.\n")
        return

    if not os.path.isdir(folder):
        print("The given path is not a folder.\n")
        return

    # Scan only the direct contents of the folder.
    items = os.listdir(folder)

    total_files = 0
    total_folders = 0
    total_size = 0

    category_stats = {}

    for category in categories:
        category_stats[category] = {
            "files": 0,
            "size": 0
        }

    category_stats["Others"] = {
        "files": 0,
        "size": 0
    }

    for item in items:
        item_path = os.path.join(folder, item)

        if os.path.isfile(item_path):
            total_files += 1

            file_size = os.path.getsize(item_path)
            total_size += file_size

            file_extension = os.path.splitext(item)[1].lower()
            category = "Others"

            for category_name, extensions in categories.items():
                if file_extension in extensions:
                    category = category_name
                    break

            category_stats[category]["files"] += 1
            category_stats[category]["size"] += file_size

        elif os.path.isdir(item_path):
            total_folders += 1

    # Display the collected statistics.
    print("\n📊 Folder Statistics")
    print("----------------------------")
    print(f"📂 Folder         : {os.path.basename(os.path.normpath(folder))}")
    print(f"📄 Files          : {total_files}")
    print(f"📁 Subfolders     : {total_folders}")
    print(f"💾 Total Size     : {total_size} bytes")

    print("\n📂 File Categories")
    print("----------------------------")

    for category, stats in category_stats.items():
        if stats["files"] > 0:
            print(
                f"{category:<18}: "
                f"{stats['files']} files | "
                f"{stats['size']} bytes"
            )
    print()



while True:
    print("""
╔══════════════════════════════════╗
║        🧹 MessCleaner ✨         ║
║             v0.2.0               ║
╚══════════════════════════════════╝

1. 📄 Create File
2. 📂 View Files
3. 🗑️  Delete File
4. 📖 Read File
5. ✍️  Append Content
6. 🧹 Organize Files
7. 📊 Folder Statistics 
8. 🔍 File Information (🚧 Coming soon)
9. ↩️  Undo Last Operation (🚧 Coming soon)
10. 🚪 Exit

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
        organize_files()
    elif choice == "7":
        folder_statistics()
    elif choice == "8":
        pass
    elif choice == "9":
        pass
    elif choice == "10":
        break


    else:
        print("Invalid choice! Please try again.\n")