import cv2
import numpy as np
import time
import tkinter as tk
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import colorsys


selected_hsv_range = []

def color_chooser():
    global selected_hsv_range
    color = askcolor(title="choose Cloak Color")[0] #rgb tuple
    if color:
        r, g, b = [x / 255.0 for x in color] # normalize
        h, s, v = colorsys.rgb_to_hsv(r, g, b)

        # hsv convert to opencv format
        h = int(h * 179)
        s = int(s * 255)
        v = int(v * 255)

        #give tolerans in color limits 
        lower = np.array([max(h - 10, 0), 100, 100])
        upper = np.array([min(h + 10, 179), 255, 255])
        selected_hsv_range = [(lower, upper)]

        color_label.config(text=f"HSV: {lower.tolist()} - {upper.tolist()}", fg="green")
    else:
        selected_hsv_range = []
        color_label.config(text="No color selected", fg="red")

def start_invisibility():
    cap = cv2.VideoCapture(0)
    time.sleep(3)

    # Arka planı alıyoruz
    for i in range(60):
        ret, background = cap.read()
        if ret:
            background = np.flip(background, axis=1)

    messagebox.showinfo("Background Captured", "Now get ready with your color cloak!")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = np.flip(frame, axis=1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Kırmızı için HSV aralığı (iki kısım)
        final_mask = None
        for lower, upper in selected_hsv_range:
            mask = cv2.inRange(hsv, lower, upper)
            if final_mask is None:
                final_mask = mask
            else:
                final_mask += mask
        
        final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
        final_mask = cv2.dilate(final_mask, np.ones((3,3), np.uint8), iterations=1)


        # Görünmezlik etkisi
        cloak_area = cv2.bitwise_and(background, background, mask=final_mask)
        inverse_mask = cv2.bitwise_not(final_mask)
        visible_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)

        final_output = cv2.addWeighted(cloak_area, 1, visible_area, 1, 0)

        cv2.imshow("Invisible Cloak", final_output)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



root = tk.Tk()
root.title("Invisibility Cloak")
root.geometry("400x250")

label = tk.Label(root, text="Click the button to start the cloak!")
label.pack(pady=10)


choose_button = tk.Button(root, text="Color Chooser", command=color_chooser)
choose_button.pack(pady=10)

color_label = tk.Label(root, text="No color selected", fg="red")
color_label.pack(pady=5)
start_button = tk.Button(root, text="Start Invisibility", command=start_invisibility)
start_button.pack(pady=10)

root.mainloop()
