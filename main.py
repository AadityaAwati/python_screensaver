import tkinter as tk
import cv2
from PIL import Image, ImageTk
import time
from pynput import keyboard, mouse
import threading

cap = cv2.VideoCapture("screensaver.mp4")
last_activity_time = time.time()
timeout = 10

screensaver_active = False

def on_key_press(key):
    global last_activity_time
    last_activity_time = time.time()
    if screensaver_active:
        exit_screensaver()

def on_mouse_move(x, y):
    global last_activity_time
    last_activity_time = time.time()
    if screensaver_active:
        exit_screensaver()

keyboard.Listener(on_press=on_key_press).start()
mouse.Listener(on_move=on_mouse_move).start()

screensaver = tk.Tk()
screensaver.withdraw()
screensaver.attributes('-fullscreen', True)
screensaver.configure(bg='black')
screensaver.title("Python Screen-Saver")

canvas = tk.Label(screensaver)
canvas.pack(fill="both", expand=True)

def update_frame():
    if not screensaver_active:
        return

    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (screensaver.winfo_width(), screensaver.winfo_height()))
    img = ImageTk.PhotoImage(Image.fromarray(frame))

    canvas.imgtk = img
    canvas.configure(image=img)
    canvas.after(30, update_frame)

def start_screensaver():
    global screensaver_active
    screensaver_active = True
    screensaver.deiconify()
    update_frame()

def exit_screensaver():
    global screensaver_active
    screensaver_active = False
    screensaver.withdraw()

def monitor_activity():
    global last_activity_time
    while True:
        time.sleep(1)
        if not screensaver_active and time.time() - last_activity_time >= timeout:
            start_screensaver()

threading.Thread(target=monitor_activity, daemon=True).start()

screensaver.mainloop()
