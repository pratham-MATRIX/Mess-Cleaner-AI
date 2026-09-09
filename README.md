# 🧹 MessCleaner

> **A Python-based command-line file manager evolving into an intelligent file management system.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Version](https://img.shields.io/badge/Version-0.2.1-orange)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 About

**MessCleaner** is an open-source Python project designed to simplify file management through automation.

The current version provides a command-line interface for browsing directories, organizing files into categories, viewing folder statistics, retrieving detailed file and folder information, safely undoing file organization operations, maintaining persistent operation history, and recording application errors for debugging.

The long-term goal is to evolve MessCleaner into a more intelligent file management system with features such as intelligent file organization, duplicate detection, AI-assisted search, automation, advanced cleanup tools, and eventually a graphical user interface.

---

## ✨ Current Features

### 📂 1. Browse Directory

Browse a directory using a recursive tree-style display.

Features include:

* Recursive folder traversal
* Hierarchical tree structure
* 📁 Folder and 📄 file distinction
* Alphabetical sorting
* Folders displayed before files
* Clear indentation showing folder ownership
* Spacing between first-level folders for better readability

Example:

```text
📂 Downloads
├── 📁 Projects
│   ├── 📄 main.py
│   ├── 📁 data
│   │   ├── 📄 dataset.csv
│   │   └── 📄 results.csv
│   └── 📄 README.md

├── 📁 Images
│   ├── 📄 photo.jpg
│   └── 📄 wallpaper.png

└── 📄 notes.txt
```

---

### 🧹 2. Organize Files

Automatically organizes files into category-based folders according to their file extensions.

Supported categories include:

* 🖼️ Images
* 🎬 Videos
* 🎵 Music
* 📄 Documents
* 📊 Spreadsheets
* 📽️ Presentations
* 📦 Archives
* 💻 Applications
* 📚 Libraries
* 👨‍💻 Code
* 🔤 Fonts
* 🗄️ Data
* 💬 Subtitles
* 🧊 3D Models
* 📐 CAD
* 🎨 Design
* 💿 Disk Images
* 📝 Log Files
* 📁 Others

Before moving files, MessCleaner displays a preview and asks for confirmation.

If a file with the same name already exists in the destination, MessCleaner automatically generates a new filename such as:

```text
file.txt
file_1.txt
file_2.txt
```

---

### 📊 3. Folder Statistics

Displays statistics for the **direct contents** of a selected folder.

Information includes:

* Total files
* Total direct subfolders
* Total size
* File count by category
* Size of each file category

Example:

```text
📊 Folder Statistics
----------------------------
📂 Folder         : Downloads
📄 Files          : 26
📁 Subfolders     : 2
💾 Total Size     : 602.55 MB

📂 File Categories
----------------------------
Images            : 4 files | 6.54 KB
Documents         : 15 files | 5.09 MB
Spreadsheets      : 3 files | 59.72 KB
Archives          : 3 files | 597.21 MB
Code              : 1 file | 486 bytes
```

> **Note:** Folder Statistics intentionally analyzes only the direct contents of the selected folder. Recursive folder analysis is handled by the Path Information feature.

---

### 🔍 4. Path Information

Provides detailed information about a selected file or folder.

#### For files:

* File name
* Full path
* File extension
* File category
* File size
* Creation time
* Modification time
* Access time

#### For folders:

* Folder name
* Full path
* Total recursive size
* Total files
* Total subfolders
* Creation time
* Modification time
* Access time

File sizes are displayed in human-readable units such as:

```text
486 bytes
6.54 KB
5.09 MB
602.55 MB
```

---

### ↩️ 5. Undo Last Operation

MessCleaner can safely undo the most recent file-organization operation.

The system maintains structured operation records containing information such as:

```text
Original Location → New Location
```

When an operation is undone, MessCleaner:

* Identifies the most recent operation
* Restores affected files to their original locations
* Handles duplicate filenames safely
* Tracks operations that could not be completely undone
* Removes empty category folders when possible
* Preserves operation history for future use

The Undo system is designed to work together with the file organization system so that organization remains reversible and traceable.

---

### 📜 6. Persistent Operation History

MessCleaner maintains operation history in **two formats**.

#### `operations.json`

A structured machine-readable record used by MessCleaner to preserve operation data.

It stores information such as:

* Operation timestamp
* Original file location
* Destination file location
* Category folder
* Whether the category folder was created by MessCleaner

This allows the Undo system to restore previous operations without parsing human-readable text.

#### `data/operations.txt`

A human-readable version of the operation history.

It allows users to review:

* When an operation occurred
* How many files were moved
* Which files were affected
* Original locations
* Destination locations
* Categories involved
* Category-folder creation information

The JSON and TXT histories are maintained together whenever an operation is recorded.

---

### 🛡️ 7. Error Logging

MessCleaner includes a persistent application-wide error logging system.

Errors are recorded in:

```text
data/errors.log
```

When an exception occurs, the error log can contain:

* Date and time
* Python exception type
* Exact technical error message
* Human-readable explanation of what happened
* Suggested action for resolving the problem
* Python traceback

Example structure:

```text
============================================================
MessCleaner Error
============================================================

Date       : 07 Sep 2026, 07:40 PM
Error Type : PermissionError
Message    : [technical Python error message]

WHAT HAPPENED:
MessCleaner could not access the requested file.

SUGGESTED ACTION:
Check that the file is accessible and that MessCleaner
has permission to access it.

TRACEBACK:
[Python traceback]

============================================================
```

The error logging system is designed so that a failure in the logging system itself does not crash MessCleaner.

---

## 🗂️ File Categories

MessCleaner currently recognizes a wide range of file extensions.

| Category      | Examples                                             |
| ------------- | ---------------------------------------------------- |
| Images        | `.jpg`, `.png`, `.gif`, `.webp`, `.svg`              |
| Videos        | `.mp4`, `.mkv`, `.avi`, `.mov`                       |
| Music         | `.mp3`, `.wav`, `.flac`, `.aac`                      |
| Documents     | `.pdf`, `.docx`, `.txt`, `.md`                       |
| Spreadsheets  | `.xls`, `.xlsx`, `.csv`, `.ods`                      |
| Presentations | `.ppt`, `.pptx`, `.odp`                              |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`                        |
| Applications  | `.exe`, `.msi`, `.apk`, `.deb`                       |
| Libraries     | `.dll`, `.so`, `.dylib`                              |
| Code          | `.py`, `.js`, `.java`, `.cpp`, `.html`, `.css`, etc. |
| Fonts         | `.ttf`, `.otf`, `.woff`, `.woff2`                    |
| Data          | `.db`, `.sqlite`, `.parquet`, `.pkl`                 |
| Subtitles     | `.srt`, `.ass`, `.vtt`                               |
| 3D Models     | `.obj`, `.fbx`, `.blend`, `.gltf`                    |
| CAD           | `.dwg`, `.dxf`, `.step`                              |
| Design        | `.psd`, `.ai`, `.eps`, `.fig`                        |
| Disk Images   | `.iso`, `.img`, `.dmg`, `.vmdk`                      |
| Log Files     | `.log`                                               |
| Others        | Unrecognized extensions                              |

---

## 🛠️ Technologies Used

* **Python 3.x**
* `os`
* `pathlib`
* `shutil`
* `json`
* `datetime`
* `time`
* `traceback`

MessCleaner currently uses only Python's standard library and does not require external Python packages.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Pratham-Singh-Thakur/Mess-Cleaner-AI.git
```

### 2. Navigate into the project

```bash
cd Mess-Cleaner-AI
```

### 3. Run MessCleaner

```bash
python app.py
```

---

## 🗂️ Project Structure

```text
Mess-Cleaner-AI/
│
├── app.py
├── README.md
├── LICENSE
├── requirements.txt
├── operations.json
│
└── data/
    ├── operations.txt
    └── errors.log
```

### Generated Files

| File                  | Purpose                                                     |
| --------------------- | ----------------------------------------------------------- |
| `operations.json`     | Structured persistent operation history used by MessCleaner |
| `data/operations.txt` | Human-readable operation history                            |
| `data/errors.log`     | Persistent application error log                            |

> `operations.json` is kept in the project root because it is an internal data file required by MessCleaner. Users normally do not need to modify it manually.

---

## 🖥️ Main Menu

```text
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
```

---

## 📈 Project Roadmap

### Version 0.1.0

* [x] Basic command-line interface
* [x] Basic file management functionality

### Version 0.2.0 / 0.2.1

* [x] Recursive directory browser
* [x] Tree-style directory visualization
* [x] File categorization system
* [x] Category-based file organization
* [x] Duplicate filename handling
* [x] Folder statistics
* [x] Detailed file information
* [x] Detailed folder information
* [x] Human-readable file sizes
* [x] Improved timestamps
* [x] Undo Last Operation
* [x] Persistent operation history
* [x] JSON operation history
* [x] Human-readable TXT operation history
* [x] Persistent error logging
* [x] Detailed exception information and traceback logging
* [x] Error recovery for corrupted or invalid operation history

---

## 🔮 Future Development

Future versions may introduce features such as:

* 🤖 AI-assisted file organization
* 🔍 Intelligent file search
* 🧬 Duplicate file detection
* 🧹 Advanced cleanup tools
* 📊 Advanced storage analysis
* ⚙️ Automated file-management rules
* 📝 Detailed activity history
* 🛡️ Advanced error recovery
* 🖥️ Graphical User Interface
* 🚀 Performance improvements
* 🔌 Plugin/extension system

> These features are part of the long-term direction of MessCleaner and are not part of the current v0.2.1 release.

---

## 🧠 Design Philosophy

MessCleaner is being developed around a simple principle:

> **Automate repetitive file-management tasks while keeping the user informed and in control.**

The project aims to avoid blindly modifying files.

Operations should be:

* 👀 Transparent
* 🛡️ Safe
* ↩️ Reversible
* 📝 Traceable
* ⚡ Efficient

---

## 📜 License

MessCleaner is released under the **MIT License**.

See the [`LICENSE`](LICENSE) file for more information.

---

## 👨‍💻 Author

**Pratham Singh Thakur**

MessCleaner is an actively developed open-source project.

---

## ⭐ Contributing

Contributions, ideas, bug reports, and feature suggestions are welcome.

If the project is useful, consider giving the repository a ⭐ on GitHub.

---

**🧹 MessCleaner — Cleaning the mess, one file at a time. 🗿🔥**
