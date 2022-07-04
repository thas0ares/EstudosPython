#Tuplas/Listas
#         0 1 2 3               4             5
lista = [0,1,2,3, ('11-11-2020', 88,50), [5,6,7,8]]
#                                          0 1 2 3
# posição 4 -> n-1 -> 4-1 =3

print(lista[0]) #0
print(lista[-1]) # [5,6,7,8]
print(lista[-1][2]) #7

matriz =[
    [0, 1, 2], # 0 - linha 1
    [3, 4, 5], # 1 - linha 2
    [6, 7, 8]  # 2 - linha 3
#    0  1  2
#  c1  c2  c3
]

print('tamanho de linhas matriz:', len(matriz))

soma=0

for linha in range(len(matriz)): #loop de linha
    for conluna in range(len(matriz[linha])):
        soma += matriz [linha][conluna]

print(soma)