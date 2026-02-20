import cv2
import numpy as np
import pytesseract
from PIL import Image

def preprocess_image(path: str):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thr = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 5
    )
    kernel = np.ones((1, 1), np.uint8)
    clean = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel)
    return Image.fromarray(clean)

def extract_text(path: str) -> str:
    img = preprocess_image(path)
    return pytesseract.image_to_string(img, config="--oem 3 --psm 6").strip()