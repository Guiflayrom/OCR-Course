import cv2
import pytesseract
from PIL import ImageFont, Image, ImageDraw
import re
from pytesseract import Output
import numpy as np

img = cv2.imread("images/despesas.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config_tesseract = "--tessdata-dir tessdata"

dataimg = pytesseract.image_to_data(img,lang="por",config=config_tesseract,output_type=Output.DICT)

n_boxes = len(dataimg['level'])

font = 'fonts/arial.ttf'

def write_text(text,x,y,img,font,font_size,color):
    font = ImageFont.truetype(font,font_size) 
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x,y - font_size),text,font=font,fill=color)
    img = np.array(img_pil)
    return img

regex_code_dateDMY = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'


for i in range(n_boxes):
    conf = float(dataimg['conf'][i])
    if conf > 1:
        (x,y,w,h) = dataimg['left'][i],dataimg['top'][i],dataimg['width'][i],dataimg['height'][i]
        
        font_size = 0.3
        font_color = (0,0,255)
        text = dataimg['text'][i]
        if re.match(regex_code_dateDMY,text):
            cv2.rectangle(img,(x-1,y-1),(x+w,y+h+1),(0,255,0),1)
            img = write_text(text,x-1,y-2,img,font,10,font_color)
            print(text)
            
cv2.imshow('image',img)
cv2.waitKey(0)


# =============================================================================
# !tesseract --help-psm
# =============================================================================


