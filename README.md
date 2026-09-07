# 🧹 MessCleaner

> **A Python-based command-line file manager evolving into an intelligent file management system.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Version](https://img.shields.io/badge/Version-0.2.0-orange)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 About

**MessCleaner** is an open-source Python project designed to simplify file management through automation.

The project currently provides a command-line interface for organizing files, browsing directory structures, viewing folder statistics, and retrieving detailed information about files and folders.

The long-term goal is to evolve MessCleaner into a more intelligent file management system with features such as persistent operation history, safe undo functionality, intelligent file organization, duplicate detection, AI-assisted search, automation, and eventually a graphical user interface.

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

## 🚧 Upcoming Features

### ↩️ Undo Last Operation

MessCleaner will support safely undoing the most recent file-management operation.

The planned system will maintain structured operation history so that MessCleaner knows exactly:

```text
Original Location → New Location
```

The Undo system will also verify files and destinations before restoring them to prevent accidental overwriting or data loss.

---

### 📝 Persistent Operation History

MessCleaner will maintain two forms of operation history:

#### `operations.log`

A human-readable log that allows users to see:

* When an operation happened
* What operation was performed
* Which files were affected
* Where files were moved

#### `operations.json`

A structured machine-readable record designed for MessCleaner itself.

This will allow the Undo system to retrieve previous operations without having to parse human-readable log text.

---

### 🛡️ Error Logging

A dedicated error log system is planned.

Whenever an exception is caught, MessCleaner will record useful information such as:

* Date and time
* Operation/function
* File or path involved
* Error message

Planned structure:

```text
logs/
├── operations.log
├── operations.json
└── errors.log
```

This will make troubleshooting and debugging much easier.

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
* `datetime`

The project currently uses Python's standard library without requiring external packages.

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
python main.py
```

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
5. ↩️  Undo Last Operation (🚧 Coming soon)
6. 🚪 Exit
```

---

## 📈 Project Roadmap

### Version 0.1.0

* [x] Basic command-line interface
* [x] Basic file management functionality

### Version 0.2.0

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
* [ ] Undo Last Operation
* [ ] Persistent operation history
* [ ] Error logging

### Future Versions

Potential future features include:

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
