#importando arquivo no python
from ex10.functions import quadrado
for i in range(10):
    print(f"o quadrado de {i} é {quadrado(i)}")
    #forma diferentes de importar uma função python
# No caso abaixo o arquivo .py desta esta na pasta raiz
# import functions
# for i in range(10):
#     print(f"o quadrado de {i} é {functions.quadrado(i)}")