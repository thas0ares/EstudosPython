##Lista de compras

from operator import itemgetter
from string import octdigits


lista_de_compras = [
    ('Camiseta', 19.90),
    ('Calca Jeans', 20.50),
    ('Meias G', 5.90)
]

#Problema: Qual é o total desse carrinho de compras?

# tupla[0] => nome do item
# tupla[1] => preço
#len -> captura o tamanho de uma lista de dados

#1: tamanho da lista

print('resoluçã com while')
#1: definir as variáveis de controle
indice = 0
#2: definir uma variavel para armazenar a soma/total
total_de_compras =0
#3: percorrerc cada item da lista
while indice < len(lista_de_compras):
    #3.1: Acessamos o valor de preço de cada item e acumulamos uma variácel total_de_compras
    total_de_compras += lista_de_compras[indice][1]
    indice += 1

print(f'O total de compras do seu carrinho : {total_de_compras}')

print('resolução com for')

total =0 

for compra in lista_de_compras:
    total += compra[1]

print(f'O total de compras do seu carrinho : {total}')

#1 compra = lista de compras[0] (assume de forma sequencial o valor da lista_de_compras)
#   total += compra[1]
#2 compra = lista de compras[1]
#   total += compra[1]


