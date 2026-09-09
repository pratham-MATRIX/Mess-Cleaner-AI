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
import json
from pathlib import Path
from datetime import datetime
import time
import traceback

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

# Store the history of file operations for Undo
operation_history = []

# Folder where MessCleaner.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder used to store MessCleaner data
DATA_FOLDER = os.path.join(BASE_DIR, "data")

# Files used for persistent operation history
OPERATIONS_JSON = os.path.join(BASE_DIR, "operations.json")
OPERATIONS_TXT = os.path.join(DATA_FOLDER, "operations.txt")

# File used to store persistent error logs
ERROR_LOG = os.path.join(DATA_FOLDER, "errors.log")

# Save operation history to JSON and TXT files
def save_operation_history():
    try:
        os.makedirs(DATA_FOLDER, exist_ok=True)

        with open(OPERATIONS_JSON, "w", encoding="utf-8") as file:
            json.dump(operation_history, file, indent=4)

        with open(OPERATIONS_TXT, "w", encoding="utf-8") as file:
            file.write("MessCleaner Operation History\n")
            file.write("=" * 60 + "\n\n")

            for index, operation in enumerate(operation_history, start=1):
                file.write(f"Operation #{index}\n")
                file.write("-" * 60 + "\n")
                file.write(f"Date       : {operation['timestamp']}\n")
                file.write(f"Files moved: {len(operation['moves'])}\n\n")


                for move in operation["moves"]:
                    file.write(
                        f"Original    : {move['original']}\n"
                        f"Destination : {move['destination']}\n"
                        f"Category    : {move['category_folder']}\n"
                        f"Created     : {move['created_category_folder']}\n\n"
                    )

                file.write("=" * 60 + "\n\n")

    except Exception as e:
        print(f"Could not save operation history: {e}")

        log_error(
            e,
            human_message=(
                "MessCleaner could not save the operation history "
                "to its persistent history files."
            ),
            action=(
                "Check that the data folder is accessible and that "
                "MessCleaner has permission to write to it."
            )
        )


# Save errors to the persistent error log
def log_error(error_message, human_message=None, action=None):
    try:
        os.makedirs(DATA_FOLDER, exist_ok=True)

        timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")

        # Get the current Python exception information
        exception_type = "Unknown"
        traceback_details = "No traceback available."

        if isinstance(error_message, Exception):
            exception_type = type(error_message).__name__
            traceback_details = traceback.format_exc()
            technical_message = str(error_message)

        else:
            technical_message = str(error_message)

        with open(ERROR_LOG, "a", encoding="utf-8") as file:
            file.write("=" * 60 + "\n")
            file.write("MessCleaner Error\n")
            file.write("=" * 60 + "\n\n")

            file.write(f"Date       : {timestamp}\n")
            file.write(f"Error Type : {exception_type}\n")
            file.write(f"Message    : {technical_message}\n\n")

            if human_message:
                file.write("WHAT HAPPENED:\n")
                file.write(f"{human_message}\n\n")

            if action:
                file.write("SUGGESTED ACTION:\n")
                file.write(f"{action}\n\n")

            file.write("TRACEBACK:\n")
            file.write(f"{traceback_details}\n")

            file.write("=" * 60 + "\n\n")

    except Exception:
        # Error logging itself should never crash MessCleaner.
        pass


# Load operation history from the JSON file
def load_operation_history():
    global operation_history

    try:
        if not os.path.exists(OPERATIONS_JSON):
            operation_history = []
            return

        with open(OPERATIONS_JSON, "r", encoding="utf-8") as file:
            loaded_history = json.load(file)

        # Make sure the loaded data is a list
        if not isinstance(loaded_history, list):
            raise ValueError("Operation history must be a list.")

        # Validate the basic structure of every operation
        for operation in loaded_history:
            if not isinstance(operation, dict):
                raise ValueError("Invalid operation format in history.")

            if "timestamp" not in operation or "moves" not in operation:
                raise ValueError("Operation is missing required fields.")

            if not isinstance(operation["moves"], list):
                raise ValueError("Operation moves must be a list.")

            for move in operation["moves"]:
                if not isinstance(move, dict):
                    raise ValueError("Invalid move format in history.")

                required_fields = [
                    "original",
                    "destination",
                    "category_folder",
                    "created_category_folder"
                ]

                for field in required_fields:
                    if field not in move:
                        raise ValueError(
                            f"Move is missing required field: {field}"
                        )

        # History is valid
        operation_history = loaded_history

    except json.JSONDecodeError as e:
        print("\n⚠️ Operation history file is corrupted.")
        print("Starting with an empty operation history.\n")

        log_error(
            e,
            human_message=(
                "MessCleaner could not load the operation history "
                "because the history file contains invalid JSON data."
            ),
            action=(
                "Restore a valid operations.json file or run MessCleaner "
                "again after fixing the file."
            )
        )

        operation_history = []

    except (ValueError, TypeError) as e:
        print("⚠️ Operation history contains invalid data.")
        print("Starting with an empty operation history.\n")

        log_error(
            e,
            human_message=(
                "MessCleaner could not load the operation history "
                "because the saved history contains invalid data."
            ),
            action=(
                "Check operations.json for missing or incorrectly formatted "
                "operation data."
            )
        )

        operation_history = []

    except OSError as e:
        print("⚠️ Could not access operation history file.")
        print("Starting with an empty operation history.\n")

        log_error(
            e,
            human_message=(
                "MessCleaner could not access the operation history file."
            ),
            action=(
                "Check that the file exists and that MessCleaner has "
                "permission to read it."
            )
        )

        operation_history = []

    except Exception as e:
        print("⚠️ Could not load operation history.")
        print("Starting with an empty operation history.\n")

        log_error(
            e,
            human_message=(
                "MessCleaner encountered an unexpected problem "
                "while loading the operation history."
            ),
            action=(
                "Check the technical details in errors.log. "
                "If the problem continues, report the error to the developer."
            )
        )

        operation_history = []


# Display saved operation history
def view_operation_history():
    if not operation_history:
        print("No operation history found.\n")
        return

    print("\n📜 Operation History")
    print("=" * 60)

    for index, operation in enumerate(operation_history, start=1):
        print(f"\nOperation #{index}")
        print("-" * 60)
        print(f"Date       : {operation['timestamp']}")
        print(f"Files moved: {len(operation['moves'])}\n")

        for move in operation["moves"]:
            print(f"📄 {os.path.basename(move['original'])}")
            print(f"   From : {move['original']}")
            print(f"   To   : {move['destination']}")
            print(f"   Category : {move['category_folder']}")
            print(
                f"   Created Folder : "
                f"{move['created_category_folder']}"
            )
            print()

    print("=" * 60 + "\n")


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
        print(f"{file:<20} ⟶  {category}/{destination_name}")

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

    # Store all successful moves from this organize operation
    current_operation = {
        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "moves": []
        }

    # Track whether this operation has been added to history
    operation_registered = False

    try:
        for file, category, file_path, destination in organized_files:
            try:
                category_path = os.path.dirname(destination)

                category_folder_existed = os.path.exists(category_path)

                os.makedirs(category_path, exist_ok=True)

                created_category_folder = not category_folder_existed

                # Move the file
                shutil.move(file_path, destination)

                # Record the move only after it succeeds
                current_operation["moves"].append({
                    "original": file_path,
                    "destination": destination,
                    "category_folder": category_path,
                    "created_category_folder": created_category_folder
                })

                # Register this operation in history after the
                # first successful move.
                if not operation_registered:
                    operation_history.append(current_operation)
                    operation_registered = True

                # Save history immediately after every successful move
                save_operation_history()

                destination_name = os.path.basename(destination)

                print(
                    f"{file} ⟶  "
                    f"{category}/{destination_name}"
                )

            except Exception as e:
                print(f"Could not move {file}: {e}")

                log_error(
                    e,
                    human_message=(
                        f"MessCleaner could not move the file "
                        f"'{os.path.basename(file)}' to its destination."
                    ),
                    action=(
                        "Check that the file still exists, is not being used by "
                        "another program, and that MessCleaner has permission "
                        "to access the source and destination folders."
                    )
                )

        print("\nOrganization completed.\n")

    except KeyboardInterrupt:
        print("\n\n⚠️ Organization interrupted by user.")

        log_error(
            "Organization interrupted by user.",
            human_message=(
                "File organization was manually interrupted before "
                "the operation could finish."
            ),
            action=(
                "No action is required if the interruption was intentional. "
                "Check operation history if you need to review what was moved."
            )
        )

        # Save everything that was successfully moved before interruption
        if current_operation:
            if not operation_registered:
                operation_history.append(current_operation)

            save_operation_history()

            print(
            f"💾 Saved {len(current_operation['moves'])} successful move(s) "                "to operation history."
            )

        print(
            "The successfully moved files can still be restored "
            "using Undo.\n"
        )

    except Exception as e:
        print(f"\n⚠️ Organization stopped unexpectedly: {e}")

        log_error(
            e,
            human_message=(
                "MessCleaner encountered an unexpected error while "
                "organizing files."
            ),
            action=(
                "Check the technical details in errors.log. "
                "If the problem continues, report the error to the developer."
            )
        )

        # Save everything that was successfully moved before the error
        if current_operation:
            if not operation_registered:
                operation_history.append(current_operation)

            save_operation_history()

            print(
                f"💾 Saved {len(current_operation['moves'])} successful move(s) "
                "to operation history."
            )

        print()


# Undo the most recent file organization operation
def undo_last_operation():
    if not operation_history:
        print("Nothing to undo.\n")
        return

    # Get the most recent operation
    last_operation = operation_history[-1]

    print("\nUndoing last operation...\n")

    remaining_operations = []

    for operation in reversed(last_operation["moves"]):
        original = operation["original"]
        destination = operation["destination"]
        category_folder = operation["category_folder"]
        created_category_folder = operation["created_category_folder"]

        try:
            if not os.path.exists(destination):
                print(
                    f"Could not undo {os.path.basename(destination)}: "
                    "file no longer exists."
                )
                remaining_operations.append(operation)
                continue

            # Make sure the original location is still available
            if os.path.exists(original):
                print(
                    f"Could not undo {os.path.basename(destination)}: "
                    "a file already exists at the original location."
                )
                remaining_operations.append(operation)
                continue

            # Check whether the original folder still exists
            original_folder = os.path.dirname(original)

            if not os.path.exists(original_folder):
                print(
                    f"\n⚠️ Original folder does not exist:"
                    f"\n{original_folder}"
                )

                while True:
                    recreate = input("Recreate the folder? (y/n): ").lower().strip()

                    if recreate == "y":
                        os.makedirs(original_folder, exist_ok=True)
                        break

                    elif recreate == "n":
                        print(
                            f"Skipped {os.path.basename(destination)}."
                        )
                        remaining_operations.append(operation)
                        break

                    else:
                        print("Invalid choice. Please enter y or n.")

                # If user chose not to recreate, move to next file
                if recreate == "n":
                    continue

            # Move the file back to its original location
            shutil.move(destination, original)

            print(
                f"{os.path.basename(destination)}  ↩️    "
                f"{original_folder}"
            )

            # Remove empty category folder if MessCleaner created it
            if created_category_folder:
                try:
                    if os.path.exists(category_folder) and not os.listdir(category_folder):
                        os.rmdir(category_folder)
                        print(
                            f"🗑️ Removed empty folder: "
                            f"{os.path.basename(category_folder)}\n"
                        )
                except OSError as e:
                    print(
                        f"Could not remove empty folder "
                        f"{os.path.basename(category_folder)}: {e}"
                    )

                    log_error(
                        e,
                        human_message=(
                            f"MessCleaner successfully restored the files, "
                            f"but could not remove the now-empty category folder "
                            f"'{os.path.basename(category_folder)}'."
                        ),
                        action=(
                            "Check whether the folder is still empty and whether "
                            "another program is using it. The folder can also be "
                            "removed manually if necessary."
                        )
                    )

        except Exception as e:
            print(
                f"Could not undo {os.path.basename(destination)}: {e}"
            )

            log_error(
                e,
                human_message=(
                    f"MessCleaner could not restore the file "
                    f"'{os.path.basename(destination)}' "
                    f"to its original location."
                ),
                action=(
                    "Check that the destination file still exists, "
                    "the original folder is accessible, and that "
                    "MessCleaner has permission to move the file."
                )
            )

            # Keep failed operations so they can be retried
            remaining_operations.append(operation)

    # Remove the old operation from history
    operation_history.pop()

    # Put failed operations back into history
    if remaining_operations:
        remaining_operations.reverse()

        last_operation["moves"] = remaining_operations
        operation_history.append(last_operation)

        # Save the updated history after a partial Undo
        save_operation_history()

        print(
            "\n⚠️ Some files could not be undone."
            "\nThey remain in history for another Undo attempt.\n"
        )
    else:
        # Save the updated history after a successful Undo
        save_operation_history()

        print("\nUndo completed.\n")


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

    except PermissionError as e:
        print("Permission denied. Cannot access this path.\n")

        log_error(
            e,
            human_message=(
                "MessCleaner could not access the requested path "
                "because permission was denied."
            ),
            action=(
                "Check that the path is accessible and that MessCleaner "
                "has permission to read it."
            )
        )

    except OSError as e:
        print(f"Could not retrieve information: {e}\n")

        log_error(
            e,
            human_message=(
                "MessCleaner could not retrieve information about "
                "the requested path."
            ),
            action=(
                "Check that the path exists, is accessible, and that "
                "MessCleaner has permission to read it."
            )
        )


# Load saved operation history when MessCleaner starts
load_operation_history()


while True:
    print("""
╔══════════════════════════════════╗
║        🧹 MessCleaner ✨         ║
║             v0.2.1               ║
╚══════════════════════════════════╝


1. 📂 Browse Directory
2. 🧹 Organize Files
3. 📊 Folder Statistics 
4. 🔍 Path Information 
5. ↩️  Undo Last Operation
6. 📜 View Operation History
7. 🚪 Exit

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
        undo_last_operation()
    elif choice == "6":
        view_operation_history()
    elif choice == "7":
        print("Exiting...\n")
        time.sleep(0.5)
        print("qwertyuioplkjhgfsaddddddd")
        break