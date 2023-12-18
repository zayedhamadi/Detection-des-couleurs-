import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]]) 
    hsv_c = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsv_c[0][0][0] 

    if 15 <= hue <= 45:  
        lower_limit = np.array([hue - 15, 100, 100], dtype=np.uint8)
        upper_limit = np.array([hue + 15, 255, 255], dtype=np.uint8)
    elif 60 <= hue <= 150:  
        lower_limit = np.array([hue - 30, 100, 100], dtype=np.uint8)
        upper_limit = np.array([hue + 30, 255, 255], dtype=np.uint8)
    elif 165 <= hue <= 180 or 0 <= hue <= 15 or 0 <= hue <= 7:
        lower_limit = np.array([0, 100, 100], dtype=np.uint8)
        upper_limit = np.array([15, 255, 255], dtype=np.uint8)
    else:
        lower_limit = np.array([0, 0, 0], dtype=np.uint8)
        upper_limit = np.array([0, 0, 0], dtype=np.uint8)

    return lower_limit, upper_limit

