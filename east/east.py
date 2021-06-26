import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import pytesseract

detector = 'frozen_east_text_detection.pb'
largura, altura = 320, 320

imagem = 'images/caneca.png'
min_confianca = 0.9

img = cv2.imread(imagem)
original = img.copy()

H = img.shape[0]
W = img.shape[1]

proporcao_W = W / float(largura)
proporcao_H = H / float(altura)

img = cv2.resize(img, (largura, altura))
H = img.shape[0]
W = img.shape[1]

nomes_camadas = ['feature_fusion/Conv_7/Sigmoid', 'feature_fusion/concat_3']

rede_neural = cv2.dnn.readNet(detector)

blob = cv2.dnn.blobFromImage(img, 1.0, (W, H), swapRB = True, crop = False)

rede_neural.setInput(blob)
scores, geometry = rede_neural.forward(nomes_camadas)

linhas, colunas = scores.shape[2:4]

caixas = []
confiancas = []

def dados_geometricos(geometry, y):
  xData0 = geometry[0, 0, y]
  xData1 = geometry[0, 1, y]
  xData2 = geometry[0, 2, y]
  xData3 = geometry[0, 3, y]
  data_angulos = geometry[0, 4, y]
  return data_angulos, xData0, xData1, xData2, xData3

def calculos_geometria(data_angulos, xData0, xData1, xData2, xData3):
  (offsetX, offsetY) = (x * 4.0, y * 4.0)
  angulo = data_angulos[x]
  cos = np.cos(angulo)
  sin = np.sin(angulo)
  h = xData0[x] + xData2[x]
  w = xData1[x] + xData3[x]

  fimX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
  fimY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
  
  inicioX = int(fimX - w)
  inicioY = int(fimY - h)

  return inicioX, inicioY, fimX, fimY

for y in range(0, linhas):
  #print(y)
  data_scores = scores[0, 0, y]

  data_angulos, xData0, xData1, xData2, xData3 = dados_geometricos(geometry, y)

  for x in range(0, colunas):
    if data_scores[x] < min_confianca:
      continue
    
    inicioX, inicioY, fimX, fimY = calculos_geometria(data_angulos, xData0, xData1, xData2, xData3)
    confiancas.append(data_scores[x])
    caixas.append((inicioX, inicioY, fimX, fimY))


deteccoes = non_max_suppression(np.array(caixas), probs=confiancas)

margem = 3
copia = original.copy()
config_tesseract = "--tessdata-dir tessdata --psm 7"

for (inicioX, inicioY, fimX, fimY) in deteccoes:
  inicioX = int(inicioX * proporcao_W)
  inicioY = int(inicioY * proporcao_H)
  fimX = int(fimX * proporcao_W)
  fimY = int(fimY * proporcao_H)

  roi = copia[inicioY - margem:fimY + margem, inicioX - margem:fimX + margem]

  texto = pytesseract.image_to_string(roi, lang='por', config=config_tesseract)
  print(texto)

  cv2.rectangle(copia, (inicioX - margem, inicioY - margem), (fimX + margem, fimY + margem), (0,255,0), 2)

cv2.imshow("copia",copia)
cv2.imshow("roi",roi)
cv2.waitKey(0)











