# 🧩 FloatingProgressBar

A floating, persistent progress bar pinned to your Windows wallpaper — track your daily tasks right from the desktop!  
Simple, lightweight, and open-source.

---

### ✅ Features

- ✅ Stays on your **desktop wallpaper layer**
- ✅ Shows a **progress bar** based on your completed tasks
- ✅ Right-click to **expand/collapse**
- ✅ Add/Delete tasks with checkboxes
- ✅ Saves your progress in a local `.json` file
- ✅ Vertical layout for minimal distraction

---

### 📦 What's Included in This Repo

- `taskbar.exe` → The executable file (ready to use)
- `taskbar.py` → The Python source code
- `tasks.json` → Your saved tasks (created automatically)
- Other runtime files needed by the `.exe`

---

### 📸 Preview
![FloatingProgressBar Preview](assets/Screenshot 2025-06-23 140855.png)

### 🚀 How to Use

#### 👉 Run the App
- Just double-click `taskbar.exe`
- You'll see a small vertical progress bar on your wallpaper
- **Right-click** it to show the task panel
- Add tasks, mark them done, and watch the progress update!

#### 🗂 Where Tasks Are Stored
- A `tasks.json` file is created next to the `.exe`
- Your data is saved here, so it's persistent even after reboots

---

### 🛠 Want to Customize or Rebuild the `.exe`?

#### 1. Install Python 3 and dependencies:

```bash
pip install pyqt5 pywin32
