from tkinter.colorchooser import askcolor
import colorsys
import numpy as np

def choose_color():
    color = askcolor(title="Choose Cloak Color")[0]
    if color:
        r, g, b = [x / 255.0 for x in color]
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        h = int(h * 179)
        s = int(s * 255)
        v = int(v * 255)
        lower = np.array([max(h - 10, 0), 100, 100])
        upper = np.array([min(h + 10, 179), 255, 255])
        return [(lower, upper)], f"HSV: {lower.tolist()} - {upper.tolist()}"
    return [], "No color selected"
