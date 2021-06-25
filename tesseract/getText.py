import cv2
import numpy as np
import pytesseract
from PIL import Image


img = cv2.imread("images/list_name.png")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config_tesseract = "--tessdata-dir tessdata --psm 6"

texto = pytesseract.image_to_string(rgb,lang="por",config=config_tesseract)

print(texto)

# =============================================================================
# open("output.txt","w",encoding="utf8").write(texto)
# =============================================================================

# =============================================================================
# !tesseract --help-psm
# =============================================================================

