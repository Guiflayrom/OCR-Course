import cv2
import pytesseract
from pytesseract import Output
from PIL import ImageFont, Image, ImageDraw
import numpy as np

img = cv2.imread("images/list_name.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
expand_pixels_y = 100
img = cv2.resize(img,(img.shape[1],img.shape[0]+expand_pixels_y))

config_tesseract = "--tessdata-dir tessdata --psm 4"

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

for i in range(n_boxes):
    conf = float(dataimg['conf'][i])
    if conf > 1:
        (x,y,w,h) = dataimg['left'][i],dataimg['top'][i],dataimg['width'][i],dataimg['height'][i]
        
        font_size = 0.3
        font_color = (0,0,255)
        text = dataimg['text'][i]
        
        # cv2.putText(img,text,(x,y+20),cv2.FONT_HERSHEY_SIMPLEX,font_size,font_color)
        cv2.rectangle(img,(x-5,y-5),(x+w,y+h+5),(0,255,0),1)
        
        img = write_text(text,x-5,y+25,img,font,10,font_color)
    
cv2.imshow('image',img)
cv2.waitKey(0)


# =============================================================================
# !tesseract --help-psm
# =============================================================================


