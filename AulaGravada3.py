#Tuplaa      ()
#Listas      []
#Dicionarios {}

#INDEX (3) -< posiçao dos itens dentro da coleção

#Index: Valor
#Chava: Valor

#nomes = [.............]
#frutas = {.. .. .. .. .. ..} #desempenho melhor, porém não trabalham com index/ chave vc não pode procurar pelo valor

#dicionario = {}

#dicionario['nome'] = 'Tiago' #dicionario na posição nome recebe tiago
#dicionario['idade'] = 25 #chave idade tem valor 25

#print(dicionario)

#print("__________________________________________________________________")

#Funções -> escrever trecho de codigo e chamar varias vezes dentro do codigo

#def multiplica(x, y):
#    resultado = x * y
#    print(resultado)

##multiplica(4, 6)

#print("__________________________________________________________________")

#lista = ['Tiago', 'Caio', 'Kaique', 'Leo']

#def checaCaio(x):
#   for nome in x:
#       if nome =='Caio':
#           return 'Sim, o Caio está na lista!'
#   return 'Não há nenheum Caio nesta lista'

#resultado = checaCaio(lista)
#print(resultado)

#print("__________________________________________________________________")
#def soma(x, y = 2): #ele utiliza o 2 quando não sinaliza
#    print(x +y)

#soma(4)

#print("__________________________________________________________________")
#def pesos(*x):  #args
#    peso_total = 0
#    for peso  in x:
#        peso_total = peso_total + peso
#    
#    print(peso_total)

#pesos(50, 60 , 70, 80)

#def pesos(**x):  #Kwargs é a mesma coisa porém para dicionarios
#    peso_total = 0
#      for peso  in x:
#        peso_total = peso_total + peso
    
#   print(peso_total)

#pesos(pesos=30, cadeira=nova)

#def pesos(*x):  #com input
#   peso_total = 0
#   for peso  in x:
#        peso_total = peso_total + peso
    
#   resposta = input('Quer saber o peso total? S/n: ')
#   if resposta == 'S':
#    print(peso_total)

#pesos(20,30)
#ou
#pesos(int(input('digite: ')))

#print("__________________________________________________________________")
#utilizando o 'import' você pode importar alguns módulos que não fazem parte da instalação do python
# import random
# print(random.randint(0,100)) gerar um número aleatório entre 0 e 100 

#podemos importar apenas a função do módulo
#from random import randint  #do módulo random importe somente randint
#print(randint(0,100))

#podemos ter acessos a outras funções/módulos por bibliotecas através de outras pessoas na internet
# import teste
# teste.soma(4,5)

# from teste import soma
# soma(4,5)

#PIP -> ferramenta que auxilia e permite que vc baixe pacotes na internet e instale no seu pc
#vc vai no terminal e pi install flask
#import flask

#print("__________________________________________________________________")

#Modos de arquivos mais usados
# w =write = Sobrescrever , nesse modo ele apaga e coloca o novo
# r =read = ler
# a =append = adicionar algo no final, não quero sobrescrever ele apenas adiciona


# arquivo = open('exemplo', 'r' ) # abrir um arquivo chamado exmeplo e dar um e após o modo 'w, a , r',
#é possivel passar o camninho de uma arquivo tbm

#conteudo = "linha secundárias" #Cria um arquivo chamado exemplo 
# conteudo = arquivo.readlines() # traz uma lista do que tem no arquivo
# print(conteudo)

#arquivo.write(conteudo)

#print("__________________________________________________________________")

#CLASSES, começam com letras maiúsculas


class PilhaDePratos: #receita de bolo para criar um objeto, se forma que vc tenha dizer o que ele vai ser e passar os metodos as ações que vc pode criar com a aquele objeto

    def _init_(self): #são métodos, inicializando,está setando e com parâmetro self
        self.pilha = []
    
    def empilhar(self):
        self.pilha.append('Prato limpo') #add item a lista
    
    def desempilhar(self):
        self.pilha.pop(-1) #remoce item da lista

    def contar(self):
        print(self.pilha)

p = PilhaDePratos()

p.empilhar()
p.empilhar()
p.empilhar()
p.desempilhar()
p.contar()