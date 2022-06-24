# LISTAs
# sempre irá aprecer entre colchetes
# pode usar várias informações dentro, qql tipo aceitável

lista = [0, 1, 3, 4, "txt", 1.5, [3, 2]]
print(lista)

lista.append('novo item')  # adicionar item
print(lista)

#insert. -> add item e quer saber qual indice/lugar

print(list[0])  # acesso via indice, primeiro elemento
print(list[-1])  # último elemento

print(lista[6])  # elemento outra lista
print(lista[6][0])  # acesso o outro lista dentro da lista

# Acesso de informações como matriz de linhas e colunas
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(matrix [0][1])
print(matrix[2][2])

#Remove o último elemento
lista.pop()
print(lista)

#print((help(lista.remove))) -> remove a primeira ocorrencia do valor que vc informou, caso não encontre ele retorna um erro, caso não tenha esse elemento que pediu para remover
lista.remove([3,2])
print(lista)

#tenho varios valores eu consigo ordenar, porém essa lista não tem como ordenar por possue numeros e string
lista_nova = [5,3,8,7,5]
lista_nova.sort()
print(lista_nova)

#deletar elementos da lista, pode fazer isso com qql indice desde que ele seja válido
del lista_nova[-1]
print(lista_nova)

#verificando o ID
lista = [0,1,2,30]
lista.append(4) #add número 4
print(id(lista)) #verifica id = 2632425419200
lista.append(5) #add número 5
print(id(lista)) # o id permanece o mesmo = 2632425419200