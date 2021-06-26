from easyocr import Reader
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

def redimensionar(largura, altura, largura_maxima = 600):
  if largura > largura_maxima:
    proporcao = largura / altura
    video_largura = largura_maxima
    video_altura = int(video_largura / proporcao)
  else:
    video_largura = largura
    video_altura = altura
  return video_largura, video_altura

def coord_caixa(caixa):
  (te, td, bd, be) = caixa
  te = (int(te[0]), int(te[1]))
  td = (int(td[0]), int(td[1]))
  bd = (int(bd[0]), int(bd[1]))
  be = (int(be[0]), int(be[1]))
  return te, td, bd, be

def desenha_caixa(img, te, bd, cor_caixa=(200, 255, 0), espessura=2): 
  cv2.rectangle(img, te, bd, cor_caixa, espessura)
  return img

def fundo_texto(texto, x, y, img, fonte, tamanho=32, cor_fundo=(200, 255, 0)):
  fundo = np.full((img.shape), (0,0,0), dtype=np.uint8)
  texto_fundo = escreve_texto(texto, x, y, fundo, fonte, (255,255,255), tamanho=tamanho)
  texto_fundo = cv2.dilate(texto_fundo,(np.ones((3,5),np.uint8)))
  fx,fy,fw,fh = cv2.boundingRect(texto_fundo[:,:,2])
  cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), cor_fundo, -1)

  return img

def escreve_texto(texto, x, y, img, fonte, cor=(50, 50, 255), tamanho=22):
  fonte = ImageFont.truetype(fonte, tamanho)
  img_pil = Image.fromarray(img) 
  draw = ImageDraw.Draw(img_pil) 
  draw.text((x, y-tamanho), texto, font = fonte, fill = cor) 
  img = np.array(img_pil) 

  return img

lista_idiomas = "en,pt"
idiomas = lista_idiomas.split(",")

gpu = False
fonte = 'content/arial.ttf'

arquivo_video = "videos/video.mp4"
cap = cv2.VideoCapture(arquivo_video)

conectado, video = cap.read()
video_largura = video.shape[1]
video_altura = video.shape[0]

video_largura, video_altura = redimensionar(video.shape[1], video.shape[0], 800)

nome_arquivo = 'output/result.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 24
saida_video = cv2.VideoWriter(nome_arquivo, fourcc, fps, (video_largura, video_altura))

amostras_exibir = 20
amostra_atual = 0

cor_fonte = (0,0,0)
cor_fundo = (200,255,0)
cor_caixa = (200,255,0)
tam_fonte = 20

while (cv2.waitKey(1) < 0):
    conectado, frame = cap.read()
    
    if not conectado:
        break 

    frame = cv2.resize(frame, (video_largura, video_altura)) 

    imagem_cp = frame.copy() 

    reader = Reader(idiomas, gpu=gpu)
    resultados = reader.readtext(frame)

    for (caixa, texto, prob) in resultados:
      te, td, bd, be = coord_caixa(caixa)

      frame = desenha_caixa(frame, te, bd)
      frame = fundo_texto(texto, te[0], te[1], frame, fonte, tam_fonte, cor_fundo)
      frame = escreve_texto(texto, te[0], te[1], frame, fonte, cor_fonte, tam_fonte)

    if amostra_atual <= amostras_exibir:
      cv2.imshow("frame",frame)
      amostra_atual = amostra_atual + 1

    saida_video.write(frame)

print("Terminou")
saida_video.release() 
cv2.destroyAllWindows()
