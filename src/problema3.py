import numpy as np
import cv2
import matplotlib.pyplot as plt
from funcoes import *

img = cv2.imread('img/cookies.tif')
cv2.imshow('Original', cv2.resize(img, None, fx=2, fy=2))

_, binary = cv2.threshold(img, 105, 255, cv2.THRESH_BINARY)
cv2.imshow('Binária', cv2.resize(binary, None, fx=2, fy=2))

# plt.imshow(binary)
# plt.show()

# Usa-se um kernel grande o suficiente para sumir com o cookie mordido
# porém pequeno o suficiente para não destruir completamente o cookie normal
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (118,118))
# Erode-se o cookie mordido completamente
removed = cv2.morphologyEx(binary, cv2.MORPH_ERODE, kernel)
cv2.imshow('Erodido cookie mordido', cv2.resize(removed, None, fx=2, fy=2))
# Dilata-se o cookie normal ao seu tamanho original
restored = cv2.morphologyEx(removed, cv2.MORPH_DILATE, kernel)
cv2.imshow('Dilatado cookie normal', cv2.resize(restored, None, fx=2, fy=2))

# Nota: isso é basicamente uma abertura

# Multiplica-se elemento a elemento a imagem original e a máscara obtida
result = img * restored
cv2.imshow('Obtido cookie normal', cv2.resize(result, None, fx=2, fy=2))

# cv2.imwrite('img/cookies.png', img)
# cv2.imwrite('img/resultado/problema3_binaria.png', binary)
# cv2.imwrite('img/resultado/problema3_removido.png', removed)
# cv2.imwrite('img/resultado/problema3_restaurado.png', restored)
# cv2.imwrite('img/resultado/problema3_resultado.png', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
