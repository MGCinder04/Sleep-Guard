import time, threading, tkinter as tk, os, psutil, pystray
from PIL import Image, ImageDraw


def create_icon():
    from PIL import Image

    return Image.open(r"C:\Python\sleep.png")


def show_popup():
    global responded
    responded = False

    def yes():
        global responded
        responded = True
        root.destroy()

    def on_close():
        global responded
        responded = True
        root.destroy()

    root = tk.Tk()
    root.title("Battery Alert")
    root.attributes("-topmost", True)

    w, h = 380, 150
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (sw - w) // 2, (sh - h) // 2 - 120
    root.geometry(f"{w}x{h}+{x}+{y}")

    frame = tk.Frame(root, bg="#d9d9d9", bd=2, relief="sunken")
    frame.pack(fill="both", expand=True)

    tk.Label(
        frame,
        text="Are you awake?",
        font=("TkDefaultFont", 12, "bold"),
        bg="#d9d9d9",
        anchor="w",
    ).pack(fill="x", padx=10, pady=(12, 2))
    tk.Label(
        frame,
        text="Laptop will shut down soon if you don’t respond.",
        font=("TkDefaultFont", 10),
        bg="#d9d9d9",
        anchor="w",
        justify="left",
    ).pack(fill="x", padx=10)

    tk.Frame(frame, height=10, bg="#d9d9d9").pack(fill="x")

    btn_frame = tk.Frame(frame, bg="#d9d9d9")
    btn_frame.pack(fill="x", side="bottom", padx=8, pady=8)
    btn = tk.Button(btn_frame, text="Yes", width=10, command=yes)
    btn.pack(side="right")
    btn.focus_set()

    root.bind("<Return>", lambda e: yes())
    root.bind("<space>", lambda e: yes())
    root.protocol("WM_DELETE_WINDOW", on_close)

    # 1-minute timeout → shutdown
    root.after(60000, lambda: (not responded) and os.system("shutdown /s /t 0"))
    root.mainloop()


def monitor():
    while True:
        battery = psutil.sensors_battery()
        percent, plugged = battery.percent, battery.power_plugged

        if (not plugged and percent <= 25) or (plugged and percent >= 100):
            t = threading.Thread(target=show_popup)
            t.start()
            t.join()

            # wait for condition to reset
            while True:
                b = psutil.sensors_battery()
                if (b.power_plugged and b.percent < 100) or (
                    not b.power_plugged and b.percent > 25
                ):
                    break
                time.sleep(30)
        time.sleep(60)


def on_quit(icon, item):
    icon.stop()
    os._exit(0)


def run_tray():
    icon = pystray.Icon(
        "SleepGuard",
        create_icon(),
        "Sleep Guard",
        menu=pystray.Menu(pystray.MenuItem("Exit", on_quit)),
    )
    threading.Thread(target=monitor, daemon=True).start()
    icon.run()


if __name__ == "__main__":
    run_tray()
