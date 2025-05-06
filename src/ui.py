import tkinter as tk
from tkinter import messagebox
import cv2

from .color_picker import choose_color
from .core import capture_background, process_frame

selected_hsv_range = []

def start_ui():
    def on_choose_color():
        global selected_hsv_range
        selected_hsv_range[:], msg = choose_color()
        color_label.config(text=msg, fg="green" if selected_hsv_range else "red")

    def start_invisibility():
        cap = cv2.VideoCapture(0)
        background = capture_background(cap)
        messagebox.showinfo("Background Captured", "Now get ready with your color cloak!")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            final_output = process_frame(frame, background, selected_hsv_range)
            cv2.imshow("Invisible Cloak", final_output)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    root = tk.Tk()
    root.title("Invisibility Cloak")
    root.geometry("400x250")

    tk.Label(root, text="Click the button to start the cloak!").pack(pady=10)
    tk.Button(root, text="Color Chooser", command=on_choose_color).pack(pady=10)

    global color_label
    color_label = tk.Label(root, text="No color selected", fg="red")
    color_label.pack(pady=5)

    tk.Button(root, text="Start Invisibility", command=start_invisibility).pack(pady=10)
    root.mainloop()
