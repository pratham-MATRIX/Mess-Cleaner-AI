"""
MessCleaner

Version : v0.2.1

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
from pathlib import Path
from datetime import datetime

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


# Calculate the total size of a folder including all subfolders
def get_folder_size(folder):
    total_size = 0

    for item in folder.rglob("*"):
        if item.is_file():
            try:
                total_size += item.stat().st_size
            except OSError:
                pass

    return total_size


# Determine the category of a file based on its extension
def get_file_category(extension):
    if not extension:
        return "No Extension"

    for category_name, extensions in categories.items():
        if extension in extensions:
            return category_name

    return "Others"


# Convert a timestamp into a readable date and time
def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime(
        "%d %b %Y, %I:%M %p"
    )


# Convert file size into a readable format
def format_size(size):
    units = ["bytes", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            if unit == "bytes":
                return f"{size} {unit}"
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


# Count files and subfolders inside a folder
def get_folder_counts(folder):
    file_count = 0
    folder_count = 0

    for item in folder.rglob("*"):
        if item.is_file():
            file_count += 1
        elif item.is_dir():
            folder_count += 1

    return file_count, folder_count


# Get formatted timestamps for a file or folder
def get_timestamps(path):
    stats = path.stat()

    return (
        format_timestamp(stats.st_ctime),
        format_timestamp(stats.st_mtime),
        format_timestamp(stats.st_atime)
    )


# Display information about a file
def display_file_information(path, extension, category, readable_size, created, modified, accessed):
    print("\n🔍 File Information")
    print("----------------------------")
    print(f"📄 Name       : {path.name}")
    print(f"📍 Full Path  : {path.resolve()}")
    print(f"📝 Extension  : {extension if extension else 'None'}")
    print(f"📂 Category   : {category}")
    print(f"📦 Size       : {readable_size}")
    print(f"📅 Created    : {created}")
    print(f"📅 Modified   : {modified}")
    print(f"📅 Accessed   : {accessed}")
    print()


# Display information about a folder
def display_folder_information(path, readable_size, file_count, folder_count, created, modified, accessed):
    print("\n🔍 Folder Information")
    print("----------------------------")
    print(f"📁 Name       : {path.name}")
    print(f"📍 Full Path  : {path.resolve()}")
    print(f"📦 Size       : {readable_size}")
    print(f"📄 Files      : {file_count}")
    print(f"📁 Subfolders : {folder_count}")
    print(f"📅 Created    : {created}")
    print(f"📅 Modified   : {modified}")
    print(f"📅 Accessed   : {accessed}")
    print()


# Display a directory and its contents as a hierarchical tree
def display_directory_tree(folder, prefix="", depth=0):
    items = sorted(
        Path(folder).iterdir(),
        key=lambda item: (item.is_file(), item.name.lower())
    )

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "

        if item.is_dir():
            print(f"{prefix}{connector}📁 {item.name}")

            # Increase indentation when displaying the contents of a subfolder
            next_prefix = prefix + ("    " if is_last else "│   ")
            display_directory_tree(item, next_prefix, depth + 1)

            # Add spacing only between first-level folders
            if depth == 0 and not is_last:
                print()

        else:
            print(f"{prefix}{connector}📄 {item.name}")

# Browse the contents of a selected directory
def browse_directory():
    folder = input("Enter directory path: ").strip()

    # Check whether the given path exists
    if not os.path.exists(folder):
        print("Folder not found.\n")
        return

    # Make sure the given path is a directory
    if not os.path.isdir(folder):
        print("The given path is not a folder.\n")
        return

    # Display the selected directory and its contents
    folder_path = Path(folder)

    print(f"\n📂 {folder_path.name}")
    print("----------------------------")

    display_directory_tree(folder_path)

    print()


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
    folder = input("Enter folder path: ").strip()

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

    category_stats = {
        category: {
            "files": 0,
            "size": 0
        }
        for category in categories
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
            category = get_file_category(file_extension)

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
    print(f"💾 Total Size     : {format_size(total_size)}")

    print("\n📂 File Categories")
    print("----------------------------")

    for category, stats in category_stats.items():
        if stats["files"] > 0:
            file_count = stats["files"]
            file_word = "file" if file_count == 1 else "files"
            print(
                f"{category:<18}: "
                f"{file_count} {file_word} | "
                f"{format_size(stats['size'])}"
            )
    print()


# Display detailed information about a file or folder
def path_information():
    path_name = input("Enter file or folder path: ").strip()
    path = Path(path_name)

    if not path.exists():
        print("File or folder not found.\n")
        return

    try:
        created, modified, accessed = get_timestamps(path)

        if path.is_file():
            extension = path.suffix.lower()
            category = get_file_category(extension)
            readable_size = format_size(path.stat().st_size)

            display_file_information(
                path,
                extension,
                category,
                readable_size,
                created,
                modified,
                accessed
            )

        elif path.is_dir():
            total_size = get_folder_size(path)
            readable_size = format_size(total_size)
            file_count, folder_count = get_folder_counts(path)

            display_folder_information(
                path,
                readable_size,
                file_count,
                folder_count,
                created,
                modified,
                accessed
            )

    except PermissionError:
        print("Permission denied. Cannot access this path.\n")

    except OSError as e:
        print(f"Could not retrieve information: {e}\n")


while True:
    print("""
╔══════════════════════════════════╗
║        🧹 MessCleaner ✨         ║
║             v0.2.0               ║
╚══════════════════════════════════╝


1. 📂 Browse Directory
2. 🧹 Organize Files
3. 📊 Folder Statistics 
4. 🔍 Path Information 
5. ↩️  Undo Last Operation (🚧 Coming soon)
6. 🚪 Exit

""")

    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        browse_directory()
    elif choice == "2":
        organize_files()
    elif choice == "3":
        folder_statistics()
    elif choice == "4":
        path_information()
    elif choice == "5":
        pass
    elif choice == "6":
        break
    else:
        print("Invalid choice! Please try again.\n")