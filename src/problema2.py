import numpy as np
import cv2
import matplotlib.pyplot as plt
from functools import reduce
from funcoes import *

img = cv2.imread('img/moire.tif')
img = img[:,:,0] # Retiro somente um canal, pois já está em escala de cinza
cv2.imshow('Original', cv2.resize(img, None, fx=2,fy=2))

h, w = img.shape
padded = np.zeros((2*h, 2*w), dtype=np.uint8)
padded[int(h/2):int(3*h/2),int(w/2):int(3*w/2)] = img

transform = fourier_transform(padded)
cv2.imshow('Transformada', exibicao(getMagDB(transform)))
# plt.matshow(getMagDB(transform))
# plt.show()

# Posição retirada da visualização da imagem
# notch_pos = (114, 160)
# Gero posições espelhadas nos 4 quadrantes
# notches = mirrorAroundCenter(notch_pos, transform)

# Gero posições dos notches
notches = [
  (108,170),
  (222,160),
  (112,328),
  (228,320),
]

# Crio filtros notch nas 4 posições
filtros = [getButterworth(notch, transform, D0=30, n=4, invert=True) for notch in notches]
# Junto os filtros
filtro = reduce(lambda a, b: a*b, filtros)
cv2.imshow('Filtro', exibicao(255*getMag(filtro)))

# Multiplico pela máscara
filtrado = np.multiply(transform, filtro)
cv2.imshow('Filtrado', exibicao(getMagDB(filtrado)))

# Faço a transformada inversa
back = inverse_transform(filtrado)[int(h/2):int(3*h/2),int(w/2):int(3*w/2)]
cv2.imshow('Resultado', cv2.resize(back, None, fx=2, fy=2))

# cv2.imwrite('img/moire.png', img)
# cv2.imwrite('img/resultado/problema2_filtrada.png', back)

cv2.waitKey(0)
cv2.destroyAllWindows()
