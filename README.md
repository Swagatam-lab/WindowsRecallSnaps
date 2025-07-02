
# 🖼️ Recall Screenshot Logger

A lightweight Python automation script inspired by Windows Recall. It captures your screen every 5 seconds and saves the screenshots in folders organized by date.

---

## 🚀 Features

- 📸 Takes automatic screenshots every 5 seconds
- 📁 Saves images into folders named by the current date (e.g., `2025-06-30`)
- 🕒 Filenames are timestamped for easy tracking
- 🖥️ Works silently in the background

---

## 📂 Folder Structure

/screenshots/
├── 2025-06-30/
│ ├── 10-00-05.png
│ ├── 10-00-10.png
│ └── ...
└── 2025-07-01/

yaml
---

## 🛠️ Requirements

- Python 3.11 (⚠️ Not compatible with 3.13+ due to `Pillow` issues)
- `pyautogui` for capturing screenshots

---

## 📦 Installation

1. **Clone the repo or download the script**
2. **Install dependencies**:

```bash
pip install pyautogui
Run the script:

bash
python screenshot_taker.py
✅ Make sure you're using Python 3.11 to avoid compatibility issues with pyautogui.

🔐 Privacy Notes
All data is saved locally on your machine

No internet access or external uploading is done

You can exclude sensitive apps by customizing the script (future feature)

🧠 Future Enhancements
OCR to extract searchable text from screenshots

Desktop app or tray icon

Screenshot filter by active window

GUI for configuration (interval, folder path, etc.)

🧑‍💻 Author
Swagatam
Python Developer | Automation Enthusiast
GitHub Profile

