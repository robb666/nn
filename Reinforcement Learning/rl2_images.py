from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
import cv2
import os


png = cv2.imread(os.getcwd() + "/screenshot.png", cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(png, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(cnts)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(thresh, (x, y), (x + w, y + h), (36, 255, 12), 1)

# # OCR
# data = pytesseract.image_to_data(gray, lang='pol')
# print(data)

cv2.imshow('thresh', thresh)
# cv2.imshow('png', png)

cv2.waitKey(0)
