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
![Screenshot 2025-06-23 140855](https://github.com/user-attachments/assets/a65e0484-ce0a-4db3-96df-f524bacb6474)

![Screenshot 2025-06-23 140914](https://github.com/user-attachments/assets/c3f26248-84be-4c71-a63e-71d39b7b3ff2)

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
