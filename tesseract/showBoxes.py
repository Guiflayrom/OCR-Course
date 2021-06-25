import cv2
import numpy as np
import pytesseract
from pytesseract import Output
# from PIL import Image
import matplotlib.pyplot as plt

img = cv2.imread("01.png")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config_tesseract = "--tessdata-dir tessdata --psm 4"

dataimg = pytesseract.image_to_data(rgb,lang="por",config=config_tesseract,output_type=Output.DICT)

n_boxes = len(dataimg['level'])

for i in range(n_boxes):
    conf = float(dataimg['conf'][i])
    if conf > 1:
        (x,y,w,h) = dataimg['left'][i],dataimg['top'][i],dataimg['width'][i],dataimg['height'][i]
        cv2.rectangle(rgb,(x,y),(x+w,y+h),(0,255,0),1)
    
cv2.imshow('image',rgb)
cv2.waitKey(0)


# =============================================================================
# !tesseract --help-psm
# =============================================================================


