# import cv2
# import numpy as np
# import pytesseract

# =============================================================================
# Invert Colors
# -- is recommended you have a white background and black words
# =============================================================================

# img = cv2.imread('images/img01.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# invert = 255 - gray

# cv2.imshow("invert",invert)
# cv2.waitKey(0)


# =============================================================================
# THRESH_BINARY
# -- manually enter a general value
# =============================================================================

# image_src = cv2.imread("images/img02.png")

# gray = cv2.cvtColor(image_src,cv2.COLOR_BGR2GRAY)

# val, tresh = cv2.threshold(gray,135,255,cv2.THRESH_BINARY)

# cv2.imshow("tresh",tresh)
# cv2.waitKey(0)


# =============================================================================
# THRESH_OTSU
# -- will try find the best general value
# =============================================================================

# image_src = cv2.imread("images/img02.png")

# gray = cv2.cvtColor(image_src,cv2.COLOR_BGR2GRAY)

# val, otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# cv2.imshow("otsu",otsu)
# cv2.waitKey(0)


# =============================================================================
# adaptiveThreshold
# -- will try show us differents values and not only one
# =============================================================================

# img = cv2.imread('images/img03.png')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adapt_media = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)

# cv2.imshow("adaptiveThreshold",adapt_media)
# cv2.waitKey(0)


# =============================================================================
# ADAPTIVE_THRESH_GAUSSIAN_C
# -- equals "adaptiveThreshold", but will reduce the noise (have more params)
# =============================================================================

# img = cv2.imread('images/img04.png')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adapt_media_gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)

# cv2.imshow("adapt_media_gauss",adapt_media_gauss)
# cv2.waitKey(0)


# =============================================================================
# OPENING
# =============================================================================

# img = cv2.imread('images/img06.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# erosao = cv2.erode(gray, np.ones((5, 5), np.uint8))
# abertura = cv2.dilate(erosao, np.ones((5,5), np.uint8))

# cv2.imshow("OPENING",abertura)
# cv2.waitKey(0)


# =============================================================================
# CLOSING
# =============================================================================

# img = cv2.imread('images/img07.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# dilatacao = cv2.dilate(gray, np.ones((5,5), np.uint8))
# fechamento = cv2.erode(dilatacao, np.ones((5, 5), np.uint8))

# cv2.imshow("CLOSING",fechamento)
# cv2.waitKey(0)


# =============================================================================
# Desfoque com Média
# =============================================================================

# img = cv2.imread('images/img08.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# desfoque_media = cv2.blur(gray, (5,5))
# cv2.imshow("desfoque_media",desfoque_media)
# cv2.waitKey(0)


# =============================================================================
# Desfoque Gaussiano
# =============================================================================

# img = cv2.imread('images/img08.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# desfoque_gaussiano = cv2.GaussianBlur(gray, (5, 5), 0)
# cv2.imshow("desfoque_gaussiano",desfoque_gaussiano)
# cv2.waitKey(0)


# =============================================================================
# Desfoque com Mediana
# =============================================================================

# img = cv2.imread('images/img08.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# desfoque_mediana = cv2.medianBlur(gray, 3)
# cv2.imshow("desfoque_mediana",desfoque_mediana)
# cv2.waitKey(0)


# =============================================================================
# Filtro bilateral
# =============================================================================

# img = cv2.imread('images/img08.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# desfoque_bilateral = cv2.bilateralFilter(gray, 15, 55, 45)
# cv2.imshow("desfoque_bilateral",desfoque_bilateral)
# cv2.waitKey(0)


# =============================================================================
# EXERCISE
# =============================================================================

# img = cv2.imread("images/img05.png")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
# val, otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# inverted = 255 - otsu

# config_tesseract = "--tessdata-dir tessdata"
# text_output=pytesseract.image_to_string(inverted, lang='por', config=config_tesseract)

# open("output.txt","w",encoding="utf8").write(text_output)

# cv2.imshow("Inverted",inverted)
# cv2.waitKey(0)





