from easyocr import Reader
import cv2

idiomas = ['en', 'pt']

gpu = False

img = cv2.imread('images/caneca.png')
original = img.copy()

reader = Reader(idiomas, gpu)
resultados = reader.readtext(img)

def coordenada_caixa(caixa):
  (te, td, bd, be) = caixa
  te = (int(te[0]), int(te[1]))
  td = (int(td[0]), int(td[1]))
  bd = (int(bd[0]), int(bd[1]))
  be = (int(be[0]), int(be[1]))
  return te, td, bd, be

coordenada_caixa(resultados[0][0])

def desenha_caixa(img, te, bd, cor_caixa=(200,255,0), espessura=2):
  cv2.rectangle(img, te, bd, cor_caixa, espessura)
  return img

img = original.copy()
for (caixa, texto, probabilidade) in resultados:
  te, td, bd, be = coordenada_caixa(caixa)
  img = desenha_caixa(img, te, bd)

cv2.imshow("img",img)
cv2.waitKey(0)












