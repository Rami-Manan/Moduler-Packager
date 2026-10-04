<div align="center">

# 📔 Personal Journal Manager

### Write Your Thoughts. Save Your Memories. 💙

A beginner-friendly, menu-driven Python application for creating, viewing, searching, and deleting personal journal entries. Each entry is saved with a timestamp in a local text file.

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation and Setup](#-installation-and-setup)
- [Usage](#-usage)
- [Example Console Interaction](#-example-console-interaction)
- [Learning Outcomes](#-learning-outcomes)
- [Future Improvements](#-future-improvements)
- [Why This Project?](#-why-this-project)
- [Support](#-support)
- [Author](#-author)

---

## 🌟 About the Project

**Personal Journal Manager** is a simple command-line application built with Python. It allows users to maintain a digital journal directly from the terminal without requiring a database or external packages.

Journal entries are stored in a file named `journal.txt`. Every new entry is automatically prefixed with the current date and time, making it easier to keep track of when thoughts and memories were recorded.

This project demonstrates how Python classes, functions, file handling, exception handling, date and time operations, and menu-driven programming can work together in a practical application.

## ✨ Features

- ✍️ **Add a New Entry** — Write and save a journal entry.
- 🕒 **Automatic Timestamps** — Each entry includes the date and time it was created.
- 📖 **View All Entries** — Display saved journal entries in the terminal.
- 🔍 **Search Entries** — Find entries by a keyword or date.
- 🗑️ **Delete All Entries** — Remove the journal file after confirmation.
- 🔁 **Interactive Menu** — Choose actions from a numbered menu.
- 🛡️ **Basic Error Handling** — Handles invalid menu input and common file errors.
- 📄 **Local Text Storage** — Stores entries in `journal.txt` in the working directory.

## ⚙️ How It Works

1. The program displays a welcome message and a menu.
2. The user selects an option from the menu.
3. The `journalmanager` class performs the selected operation.
4. Entries are saved to or read from `journal.txt`.
5. The menu repeats until the user selects **Exit**.

### Available Operations

| Option | Operation | Description |
|---|---|---|
| 1 | Add a New Entry | Saves a new entry with a timestamp. |
| 2 | View All Entries | Displays the contents of the journal file. |
| 3 | Search for an Entry | Searches entry text and timestamps for a keyword. |
| 4 | Delete All Entries | Deletes the journal file after confirmation. |
| 5 | Exit | Closes the application. |

## 🧰 Technologies Used

- **Python 3**
- `datetime` — Generates formatted timestamps.
- `os` — Removes the journal file when requested.
- **Text file handling** — Saves and reads journal entries.
- **Object-Oriented Programming (OOP)** — Groups journal operations in a class.

No third-party Python packages are required.

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── journal_manager.py   # Main Python program
├── journal.txt          # Created automatically when the first entry is saved
└── README.md            # Project documentation
```

> The Python filename shown above is an example. Use the actual filename you saved your code as.

## 📋 Requirements

- Python 3.8 or newer recommended
- A terminal or command prompt
- Any Python editor, such as VS Code

## 🚀 Installation and Setup

### 1. Clone the Repository

Replace the placeholder URL with your repository URL.

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the Project Folder

```bash
cd YOUR-REPOSITORY
```

Alternatively, open the folder directly in Visual Studio Code.

### 3. Run the Program

If your Python file is named `journal_manager.py`, run:

```bash
python journal_manager.py
```

On some systems, you may need:

```bash
python3 journal_manager.py
```

No package installation is needed because the program uses Python's standard library.

## 🖥️ Usage

When the program starts, choose an option from the main menu:

```text
Welcome to Personal Journal Manager!
Please select an option.

1. Add a New Entry
2. View all Entries
3. Search for an Entry
4. Delete all Entries
5. Exit
user Input:
```

### ✍️ Add a New Entry

Select `1` and type your journal entry.

```text
Enter your journal entry:
Today I learned how to use file handling in Python.
Entry added successfully.
```

The saved line will look similar to this:

```text
[2026-10-04 20:30:15] Today I learned how to use file handling in Python.
```

*The timestamp above is an example; the program uses the actual date and time when you create an entry.*

### 📖 View All Entries

Select `2` to display all entries saved in `journal.txt`.

```text
Your Journal Entries:
-------------------------------------
[2026-10-04 20:30:15] Today I learned how to use file handling in Python.
```

### 🔍 Search for an Entry

Select `3`, then enter a keyword or date.

```text
Enter keyword or date to search: Python
[2026-10-04 20:30:15] Today I learned how to use file handling in Python.
```

The search is case-insensitive and checks each complete saved line.

### 🗑️ Delete All Entries

Select `4` to request deletion of all journal entries.

```text
Are you sure you want to delete all entries? (yes/no): yes
All journal entries have been deleted.
```

**Warning:** Confirming deletion removes `journal.txt`, including all entries stored in it. Keep a backup if you want to preserve your journal.

### 🚪 Exit

Select `5` to close the application.

```text
Thank you for using Personal Journal Manager. Goodbye!
```

## 🎓 Learning Outcomes

By building this project, you can practise:

- ✅ Object-Oriented Programming and classes
- ✅ Constructors and instance attributes
- ✅ Functions and method calls
- ✅ File handling: reading, appending, and deleting files
- ✅ Exception handling with `try` and `except`
- ✅ Date and time formatting using `datetime`
- ✅ Conditional statements and loops
- ✅ User input validation
- ✅ Case-insensitive string searching
- ✅ Building a menu-driven command-line application

## 🌱 Future Improvements

Possible features for future versions include:

- 🔐 Password protection for private entries
- 🏷️ Categories and tags
- 📅 Calendar-based journal browsing
- ✏️ Edit an existing entry
- 🧾 Delete a selected entry instead of all entries
- 📤 Export entries to PDF or JSON
- 😊 Mood tracking
- 🔎 Search by date range
- 🖥️ A graphical user interface (GUI)
- 🗄️ SQLite database storage
- ☁️ Encrypted backup and cloud synchronisation

## ⭐ Why This Project?

Personal Journal Manager is a small but practical beginner Python project. It turns basic concepts—classes, loops, conditions, timestamps, and file handling—into a useful application.

It is suitable for learners who want to move from individual Python exercises to a complete project that can be documented and shared on GitHub.

## 🌟 Support

If you find this project useful:

- ⭐ Star the repository.
- 🍴 Fork it and experiment with new features.
- 💻 Run the project and explore how it works.
- 📣 Share it with other Python learners.

---

## 👤 Author

**[Manan Rami]**

🐍 Python Learner | 💻 Programmer

- GitHub: [Your GitHub Profile](https://github.com/)

> Replace the author name, GitHub username, repository URL, and example filename with your own project details before publishing.

---

<div align="center">

**Made with ❤️ and Python 🐍**

*Write your thoughts. Save your memories.*

</div>
