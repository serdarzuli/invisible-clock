
import cv2
import numpy as np
import time

def capture_background(cap, wait_time=3, frames=60):
    time.sleep(wait_time)
    background = None
    for i in range(frames):
        ret, frame = cap.read()
        if ret:
            background = np.flip(frame, axis=1)
    return background

def process_frame(frame, background, hsv_range):
    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    final_mask = None
    for lower, upper in hsv_range:
        mask = cv2.inRange(hsv, lower, upper)
        final_mask = mask if final_mask is None else final_mask + mask

    final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
    final_mask = cv2.dilate(final_mask, np.ones((3,3), np.uint8), iterations=1)

    cloak_area = cv2.bitwise_and(background, background, mask=final_mask)
    inverse_mask = cv2.bitwise_not(final_mask)
    visible_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    return cv2.addWeighted(cloak_area, 1, visible_area, 1, 0)
