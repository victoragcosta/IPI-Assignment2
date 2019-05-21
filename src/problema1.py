import numpy as np
import cv2
from funcoes import *

def quest1_1(img, verbose=False):
  # O kernel precisa ser pelo menos maior que a largura das letras
  kernel = np.ones((9,9), dtype=np.uint8)

  # Utiliza-se a transformada bottom-hat, pois quero realçar elementos
  # escuros em fundo claro
  bottomhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
  if verbose:
    cv2.imshow('Bottom Hat', cv2.resize(bottomhat, None, fx=0.5, fy=0.5))

  # Binariza-se a imagem em um threshold que não tenha o ruído
  _, binary = cv2.threshold(bottomhat, 45, 255, cv2.THRESH_BINARY_INV)
  if verbose:
    cv2.imshow('Binary', cv2.resize(binary, None, fx=0.5, fy=0.5))
  return binary

def quest1_2(img, verbose=False):
  # Aplico abertura seguido de fechamento para suavizar os elementos
  # escuros, sobrando só o fundo
  kernel = np.ones((15,15), dtype=np.uint8)
  opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
  if verbose:
    cv2.imshow('Opening', cv2.resize(opening, None, fx=0.5, fy=0.5))

  kernel = np.ones((25,25), dtype=np.uint8)
  background = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
  if verbose:
    cv2.imshow('Background', cv2.resize(background, None, fx=0.5, fy=0.5))

  # Subtraio da imagem o fundo obtido
  subtract = img-background
  if verbose:
    cv2.imshow('Subtract background', cv2.resize(subtract, None, fx=0.5, fy=0.5))

  # Binarizo a imagem em um threshold suficientemente grande para remover o
  # máximo de ruído possível, mas sem deteriorar as letras
  _, binary = cv2.threshold(subtract, 150, 255, cv2.THRESH_BINARY_INV)
  if verbose:
    cv2.imshow('Binary', cv2.resize(binary, None, fx=0.5, fy=0.5))
  return binary

def quest1_3(img, verbose=False):

  # Aplica-se este filtro para tentar filtrar um pouco o ruído
  kernel = np.ones((3,3), dtype=np.uint8)
  filtered = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
  # cv2.imwrite('img/resultado/problema1_filtrado.png', filtered)
  if verbose:
    cv2.imshow('Filtered', cv2.resize(filtered, None, fx=0.5, fy=0.5))

  resultado_1 = quest1_1(filtered)
  if verbose:
    cv2.imshow('Resultado 1 filtrado', cv2.resize(resultado_1, None, fx=0.5, fy=0.5))

  resultado_2 = quest1_2(filtered)
  if verbose:
    cv2.imshow('Resultado 2 filtrado', cv2.resize(resultado_2, None, fx=0.5, fy=0.5))

  return (resultado_1, resultado_2)

def quest1_4(img, verbose=False):
  kernel = np.ones((3,3), dtype=np.uint8)
  better = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
  if verbose:
    cv2.imshow('Melhor Resultado Melhorado', cv2.resize(better, None, fx=0.5, fy=0.5))

  return better


img = cv2.imread('img/morf_test.png')
cv2.imshow('Original', cv2.resize(img, None, fx=0.5, fy=0.5))

resultado_1 = quest1_1(img, verbose=False)
cv2.imshow('Resultado 1', cv2.resize(resultado_1, None, fx=0.5, fy=0.5))
resultado_2 = quest1_2(img, verbose=False)
cv2.imshow('Resultado 2', cv2.resize(resultado_2, None, fx=0.5, fy=0.5))
resultado_3_1, resultado_3_2 = quest1_3(img, verbose=False)
cv2.imshow('Resultado 1 filtrado', cv2.resize(resultado_3_1, None, fx=0.5, fy=0.5))
cv2.imshow('Resultado 2 filtrado', cv2.resize(resultado_3_2, None, fx=0.5, fy=0.5))
resultado_4 = quest1_4(resultado_3_1, verbose=False)
cv2.imshow('Melhor Resultado Melhorado', cv2.resize(resultado_4, None, fx=0.5, fy=0.5))

# cv2.imwrite('img/resultado/problema1_resultado1.png', resultado_1)
# cv2.imwrite('img/resultado/problema1_resultado2.png', resultado_2)
# cv2.imwrite('img/resultado/problema1_resultado3_1.png', resultado_3_1)
# cv2.imwrite('img/resultado/problema1_resultado3_2.png', resultado_3_2)
# cv2.imwrite('img/resultado/problema1_resultado4.png', resultado_4)

cv2.waitKey(0)
cv2.destroyAllWindows()
