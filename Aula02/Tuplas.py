#TUPLAS
#são mais restritivas que as listas
#utiliza marcação de parenteses (), mas consegue usar apenas vírgula
#é um tipo imutável de dados, uma vez definida ela é estática, vc não adicionar mais
#o uso de tuplas é para vc ter o manejo de recursos adequados para coleções


tupla = (0,1,2,3,4)
print(tupla)

tupla2 = 1,2,3,4,5 #consegue criar apenas com vírgula
print(tupla2)

#tupla.count
#tupla.index

tupla = tupla, 6,7,8 #burlando o sistema
print(tupla)

print(id(tupla)) # o python ele registra uma identificaçao única para o registro de dados

tupla += 9,10,11
print(tupla)

print(id(tupla)) # o número de identifcação mudou, o python joga fora a tupla antiga e substitue por informações nova, sendo que isso em listas já é diferente

print(tupla[-1]) # as formas de acesso são bem parecidas

#tuplas de registros, conjunto
tupla3 = ('julio', 34, 1561321561)
print(tupla[0])
nome, idade, cpf = tupla3 #desempacotando as informações de forma paralela, ele associa cada campo a ordem que você colocou
print(nome, idade, cpf)


