import sys
import os
import json
import win32gui
import win32con
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize

TASK_FILE = "tasks.json"

class TaskbarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(350, 100)
        self.move(30, 30)
        self.expanded = False
        self.old_pos = None

        self.setStyleSheet("background-color: #1e1e2f; color: white; border-radius: 10px;")

        self.tasks = self.load_tasks()

        self.main_layout = QVBoxLayout(self)

        # ✅ ONLY PROGRESS BAR NOW
        self.progress = QProgressBar()
        self.progress.setFixedHeight(32)
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: #333;
                border: 3px solid #444;
                border-radius: 5px;
                text-align: center;
                margin: 5px;
            }
            QProgressBar::chunk {
                background-color: aqua;
            }
        """)
        self.main_layout.addWidget(self.progress)

        # Expanded task area (hidden initially)
        self.task_area = QWidget()
        self.task_layout = QVBoxLayout(self.task_area)
        self.task_area.setVisible(False)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter new task...")
        self.task_layout.addWidget(self.task_input)

        self.add_btn = QPushButton("➕ Add Task")
        self.add_btn.clicked.connect(self.add_task)
        self.task_layout.addWidget(self.add_btn)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.task_list_widget = QWidget()
        self.task_list_layout = QVBoxLayout(self.task_list_widget)
        self.scroll.setWidget(self.task_list_widget)
        self.task_layout.addWidget(self.scroll)

        self.main_layout.addWidget(self.task_area)

        self.refresh_tasks()
        self.update_progress()

        self.pin_to_wallpaper()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()
        elif event.button() == Qt.RightButton:
            self.toggle_task_area()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def toggle_task_area(self):
        self.expanded = not self.expanded
        self.task_area.setVisible(self.expanded)
        self.setFixedHeight(400 if self.expanded else 60)

    def add_task(self):
        name = self.task_input.text().strip()
        if not name:
            return
        self.tasks.append({"name": name, "done": False})
        self.task_input.clear()
        self.save_tasks()
        self.refresh_tasks()
        self.update_progress()

    def toggle_task(self, index, checked):
        self.tasks[index]["done"] = checked
        self.save_tasks()
        self.update_progress()

    def delete_task(self, index):
        reply = QMessageBox.question(self, "Delete Task",
                                     f"Delete '{self.tasks[index]['name']}'?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.tasks.pop(index)
            self.save_tasks()
            self.refresh_tasks()
            self.update_progress()

    def refresh_tasks(self):
        for i in reversed(range(self.task_list_layout.count())):
            widget = self.task_list_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for index, task in enumerate(self.tasks):
            row = QFrame()
            layout = QHBoxLayout()
            chk = QCheckBox(task["name"])
            chk.setChecked(task["done"])
            chk.stateChanged.connect(lambda state, i=index: self.toggle_task(i, state == Qt.Checked))
            del_btn = QPushButton("🗑")
            del_btn.setFixedSize(QSize(30, 25))
            del_btn.clicked.connect(lambda _, i=index: self.delete_task(i))
            layout.addWidget(chk)
            layout.addWidget(del_btn)
            row.setLayout(layout)
            self.task_list_layout.addWidget(row)

    def update_progress(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        self.progress.setValue(int((done / total) * 100) if total > 0 else 0)

    def save_tasks(self):
        with open(TASK_FILE, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as f:
                return json.load(f)
        return []

    def pin_to_wallpaper(self):
        progman = win32gui.FindWindow("Progman", None)
        win32gui.SendMessageTimeout(progman, 0x052C, 0, 0,
                                    win32con.SMTO_NORMAL, 1000)

        def enum_handler(hwnd, result):
            if win32gui.GetClassName(hwnd) == "WorkerW":
                if win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None):
                    result.append(hwnd)

        workerws = []
        win32gui.EnumWindows(enum_handler, workerws)
        if workerws:
            workerw = workerws[0]
            hwnd = self.winId().__int__()
            win32gui.SetParent(hwnd, workerw)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TaskbarWidget()
    win.show()
    sys.exit(app.exec_())
