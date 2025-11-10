# Sleep-Guard

**Sleep Guard** is a lightweight background utility that prevents your laptop from staying on all night.
It quietly runs in the **system tray** and monitors your **battery level**:

* If the battery drops to **25% while discharging**, or
* If it reaches **100% while charging**,

you’ll get a popup asking, **“Are you awake?”**
If you don’t respond within 1 minute, the computer will **automatically shut down**.

---

### ⚙️ Features

* 🪟 **System tray support** (minimizes silently on startup)
* 🔋 **Battery monitoring** using `psutil`
* 🧠 **Smart popup** for low or full battery
* 🕐 **Auto-shutdown after 60 seconds** if no response
* 🖼️ **Custom tray icon** (`sleep.png`)
* 🚀 **Runs automatically at Windows startup**

---

### 📦 Requirements

Install the required Python libraries once:

```bash
pip install psutil pystray pillow
```

---

### 🧰 How to Use

1. Save the script as

   ```bash
   C:\Python\sleep_guard.py
   ```
2. Place your tray icon image at

   ```
   C:\Python\sleep.png
   ```
3. Run the script silently (no console window):

   ```bash
   pythonw "C:\Python\sleep_guard.py"
   ```
4. You’ll see your **Sleep Guard** 💤 icon in the system tray.

   * Right-click the tray icon → **Exit** to quit.
   * The script runs quietly in the background otherwise.

---

### 🔄 Auto-Start on Boot (Windows)

To make it launch automatically every time you log in:

1. Press **Win + R** → type:

   ```
   shell:startup
   ```
2. In the Startup folder, create a new **Shortcut** with:

   ```
   pythonw "C:\Python\sleep_guard.py"
   ```
3. Name it `Sleep Guard`.

✅ Done! Sleep Guard will now start automatically each time you log in.

---

### 📁 Project Structure

```
C:\
 └── Python\
      ├── sleep_guard.py     ← main program
      └── sleep.png          ← tray icon
```

---

### 🧩 How It Works

1. Script runs as a tray icon.
2. Every minute, it checks battery status via `psutil`.
3. If conditions match (≤25% or 100%), it shows a Tkinter popup:

   * You can click **Yes** or press **Enter/Space**.
   * If ignored for 60 seconds → shuts down system.
4. Waits for the battery level to return to normal before checking again.

---

### 🧑‍💻 Author

**Sleep Guard** by *Mohit*
A simple safety tool to prevent accidental overnight laptop use.

---
