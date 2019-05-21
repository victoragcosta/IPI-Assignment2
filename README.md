# Trabalho 2 de IPI
Desenvolvimento do trabalho de Introdução ao Processamento de Imagens da Universidade de Brasília com o objetivo de exercitar o uso de filtros no domínio da frequência e operações morfológicas para processamento de imagens.

Matrícula | Nome
----------|------------------------
160019311 | Victor André Gris Costa

# Problemas

## Questão 1
Faça um programa que utilize como entrada a imagem morf_test.png. O programa deve entregar uma imagem binária como saída, com o fundo branco e as imagens pretas. Teste, e mostre os resultados das seguintes operações no relatório:
1. A aplicação da transformada top-hat e/ou bottom-hat antes da binarização
2. Tentar criar uma imagem que seja somente o fundo (mediante operações morfológicas), e subtrair essa imagem da original.
3. Aplique filtros prévios para tentar melhorar o resultado de 2.1 e 2.2
4. No melhor resultado obtido aplique operações morfológicas binárias (tipo abertura, fechamento) para tentar evitar símbolos desconectados ou ruídos.

## Questão 2
Faça um programa para realizar o processo de filtro rejeita-notch, mediante o uso de filtros passa-altas Butterworth (com n=4). A imagem que deve ser usada é o arquivo "MOIRE.TIF". No relatório desta parte deve estar incluído:
1. Uma Figura com a imagem original
2. Uma Figura com a imagem filtrada utilizando 4 pares notch com a seguinte características (usando padding)
3. Comentários sobre os resultados obtidos.

## Questão 3
Faça um script realize os seguintes passos:
1. Ler a imagem "cookies.tif"
2. Binarizar a imagem de tal forma que sejam identificados as duas "cookies" (escolher o limiar apropriado, de forma de diferenciar as cookies do fundo).
3. Eliminar por completo a "cooky" mordida, deixando pelo menos parte da cooky completa, na imagem binarizada. Mediante algoritmo morfológico.
4. Recuperar a forma inicial da "cooky" completa na imagem resultante do passo anterior. Mediante algoritmo morfológico.
5. A partir da imagem original e utilizando a imagem resultante do passo anterior como máscara, obter uma imagem final em níveis de cinza com somente a "cooky" completa.

# Bibliotecas Usadas
* Utilizou-se [Python versão 3.7.3](https://www.python.org/downloads/release/python-373/)
* A instalação das bibliotecas pode ser feita através do comando
`pip3 install <nome da biblioteca>`

Nome          | Versão
--------------|-------------
numpy         | >= 1.16.2
opencv-python | >= 4.0.0.21
matplotlib    | >= 3.0.3

## Modo de uso
### Problema 1
1. Navegue seu shell para a pasta raiz deste projeto (onde o README.md está)
2. Execute com um desses comandos dependendo do seu sistema e configurações:
  * `python src/problema1.py`
  * `python3 src/problema1.py`
  * `python3.7 src/problema1.py`
### Problema 2
1. Navegue seu shell para a pasta raiz deste projeto (onde o README.md está)
2. Execute com um desses comandos dependendo do seu sistema e configurações:
  * `python src/problema2.py`
  * `python3 src/problema2.py`
  * `python3.7 src/problema2.py`
### Problema 3
1. Navegue seu shell para a pasta raiz deste projeto (onde o README.md está)
2. Execute com um desses comandos dependendo do seu sistema e configurações:
  * `python src/problema3.py`
  * `python3 src/problema3.py`
  * `python3.7 src/problema3.py`
