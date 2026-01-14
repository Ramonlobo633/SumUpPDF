import cv2
import numpy as np

def preprocess_image(pil_image):
    img = np.array(pil_image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
