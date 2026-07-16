# ⌨️ AutoType

**AutoType** is a lightweight Python automation tool that simulates keyboard input character-by-character — perfect for environments where copy-paste is blocked (remote desktops, secure portals, kiosk apps, and more).

---

## 🚀 Features

- ✅ Simulates real keystrokes, not clipboard paste
- ✅ Works in apps that block copy-paste
- ✅ Press **ENTER** to start, **ESC** to stop — no UI needed
- ✅ Adjustable typing speed
- ✅ Supports 1000+ lines of text
- ✅ Works on Windows, macOS, and Linux

---

## 📋 Requirements

- Python 3.6+
- `pyautogui`
- `keyboard`

---

## 🛠️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/HackerG3121/Auto-Type-Script-using-Python.git
cd autotype
```

**2. Install dependencies:**
```bash
pip install -r requrededpip.txt
```

> ⚠️ On Linux/macOS you may need to run with `sudo` due to keyboard hook permissions.

---

## 📖 Usage

**1. Add your text to `scriptfile.txt`:**
```
This is the text that will be auto-typed.
You can add as many lines as you want.
```

**2. Run the script:**
```bash
python autotype.py
```

**3. Follow the on-screen instructions:**
- Open the target application and click inside the text field
- Press **ENTER** to begin typing (3-second delay before start)
- Press **ESC** at any time to stop

---

## ⚙️ Configuration

Inside `autotype.py`, you can adjust the typing speed:

```python
time.sleep(0.01)  # Delay between each character (in seconds)
                  # Lower = faster, Higher = slower
```

---

## 🖥️ Platform Notes

| Platform | Notes |
|----------|-------|
| **Windows** | Works out of the box. Run as Administrator if needed. |
| **macOS** | Grant Accessibility permissions in System Settings → Privacy & Security. |
| **Linux** | Run with `sudo python autotype.py` for keyboard hook access. |

---

## 📁 File Structure

```
autotype/
├── autotype.py        # Main script
├── scriptfile.txt     # Your text goes here
├── requirements.txt   # Python dependencies
├── README.md          # This file
└── LICENSE            # MIT License
```

---

## ❓ FAQ

**Q: It's not typing anything / types wrong characters.**  
A: Make sure your system keyboard layout matches. `pyautogui` uses US keyboard layout by default. You can use `pyautogui.typewrite()` or `pyautogui.write()` with `interval` for better compatibility.

**Q: The script requires Administrator mode.**  
A: Some applications (e.g., UAC prompts, certain secure apps) require elevated privileges. Right-click CMD and choose "Run as Administrator".

**Q: Can I type special characters?**  
A: Basic ASCII characters work well. Special Unicode characters may vary by platform and application.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This tool is intended for **legitimate personal use only** — such as automating repetitive input tasks in your own workflows. Do not use this tool to bypass security systems, automate inputs on platforms that prohibit it, or for any malicious purpose. The author is not responsible for any misuse.
