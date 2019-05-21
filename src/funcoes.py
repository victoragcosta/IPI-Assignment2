import numpy as np
import cv2

def getMag(transform):
  return np.abs(transform)

def getMagDB(transform):
  return 20*np.log(getMag(transform))

def getButterworth(pos,  transform, D0=1, n=4, invert=False):
  # Crio 3 matrizes com coordenadas x, y
  xx, yy = np.meshgrid(
    np.arange(transform.shape[1]),
    np.arange(transform.shape[0]),
    indexing='xy'
  )
  # Calculo parte D da função butterworth
  D = ( (xx-pos[0])**2 + (yy-pos[1])**2 )**0.5
  # Calculo a função completa
  if invert:
    butter = np.sqrt( 1/( 1+(D0/D)**(2*n) ) )
    #butter = np.vectorize(lambda a: 0 if a < D0 else 1)(D)
  else:
    butter = 1/(1+((D/D0)**(2*n)))
  # Retorno trocando preto por branco e vice-versa caso pedido
  return butter

def mirrorAroundCenter(pos, transform):
  # Gero posições em todos os quadrantes da imagem
  height, width, *a = transform.shape
  x = abs(width/2 - pos[0])
  y = abs(height/2 - pos[1])
  ret = [
    (width/2+x,height/2+y),
    (width/2-x,height/2+y),
    (width/2+x,height/2-y),
    (width/2-x,height/2-y),
  ]
  return ret

def normalize(img):
  return (img-img.min())/(img.max()-img.min())

def fourier_transform(img):
  return np.fft.fftshift(np.fft.fft2(img))

def inverse_transform(transform):
  return np.uint8(255*normalize(getMag(np.fft.ifft2(np.fft.ifftshift(transform)))))

def exibicao(transform):
  return cv2.resize(np.uint8(transform), None, fx=1, fy=1)
