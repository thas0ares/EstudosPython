#Aula realizada no dia 21/06/2022, revisão do material disponível

#print('Pão de batata') -> nós enviamos a informação, onjunto de caracteres tem que ficar entre '' "" (não tem diferença, ele identifica que é uma String) 
#input('Digite seu nome: ') -> Espera alguma informação do usuário
#nome = """Thais "Soares" 'Alves' Silva""" -> Ex: caracteres de escape
# Váriaveis -> elas contém valores

from this import d


nome = 'Thais'
idade = 30
altura = 1.80

print('Meu nome é ' + nome)
print('Meu nome é {}'.format(nome)) #modo antigo da fString, era utilizado no python2
print(f'Meu nome é {nome}, minha idade é {idade} anos' )#fString é a mesma forma de

print("__________________________________________________________________")

#Existem 4 tipos de daos no python: 
nome = 'Thais Soares' #String, txt
idade = 25 #Inteiro
Altura = 1.80 #Float, decimal (utiliza ponto e não vírgula)
Habilitado = True #Boolean, True/False (sempre letra maiúscula)

primeir_nome = nome.split() #separa os nomes das variáveis nos espaços, como listas, cada valor leva uma numeração que começa no 0
print(f'primeiro nome: {primeir_nome}') #imprime os dois
print(f'primeiro nome: {primeir_nome[0]}')# imprime apenas Thais

#altura = input('Qual sua altura?') -> o usuário pode digitar qql valor, pois os valores que o input recebe é do tipo String, mas podemos converter!!
#print(altura)

print("__________________________________________________________________")

resposta = input('Digite sim ou não: ')

if resposta == 'sim': #se a resposta for igual á sim (esse foi um teste, e sempre tem como resposta um true ou false e então ele vai resolver o que esta dentro dele) imprimima abaixo
    print('Você digitou SIM')
else: # senão imprima abaixo
    print('Você digitou NÃO')

if resposta == 'sim': #testa aqui primeiro
    print('Você digitou SIM')
elif resposta =='não': #após testa aqui, pode ter mais de um elif (junção do else e if)
    print('Você digitou NÃO')
else: # é o ultimo, porém é opicional, mas só pode ter um
    print('Você digitou outra coisa')

print("__________________________________________________________________")

#Estruturas de repetição:
for numero in range(0, 30, 2): # para cada número em um intervalo de 0 até 30, o terceiro valor é o ritmo no qual o valores são repassados no caso pulando 2
    print(numero) #imprima número

texto = "Thais Soares Alves da Silva Rossi"
lista = texto.split()

for palavra in lista:
    if palavra == 'Alves':
        print('encontrei!')

#Criando um LOOP, com uma variável de controle
resposta = 0

#while resposta == 0: #enquanto resposta for 0 repita "resposta ainda é 0"
    #print('Resposta ainda é zero!')
    #resposta = int (input('Digite um número diferente de zero: ')) #podemos CONVERTER a resposta da pessoa do input para o tipo de dado que queremos 
    #checa/valida  o que a pessoa escreve e dps converte

#sem variável de controle, repetição que roda para sempre

while True:
    resposta = input('Digite um número diferente de zero: ')
    
    if resposta != '0': # se a resposta da pessoa for diferente de 
        break 
print("__________________________________________________________________")

#Coleções -> é um conjunto de valores

#Tuplaa      ()
#Listas      []
#Dicionarios {}
#Sets        {}

#INDEX (3), indices numeros que começam em 0
#TUPLAS SÃO IMUTAVEIS
nomes = ('Thais', 'Caio', 'Kaique','amanda')
print(nomes[2]) # traz apenas Kaique, pela posição

for x in nomes: #usando como objetos de interação
    print(x)
 
#LISTAS

nomes2 = ['tiago', 'caio', 'kaique','amanda']
nomes2.pop(3) #remove itens da lista por index
nomes2.remove('caio') # remove itens por valores
nomes2.append('bruno') #adiciona um valor

print(nomes2)

print(nomes2.index('bruno')) #procura item na lista, por posição

#para procurar por determinado nome dentro da lista
for nome in nomes2: #ele vai pra cada nome que ele encontrar dentro da minha lista
    if nome == 'tiago': # ele vai chegar se é caio
        print(f'tem um tiago na lista, na posição {nomes2.index("tiago")}')# se ele achar esse nome da minha lista ele vai imprimir isso e mostrar a posição de caio