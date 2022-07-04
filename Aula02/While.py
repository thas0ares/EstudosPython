# estruturas de repetição

#While -> enquanto (enquanto uma condição não for satisfeita vc irá repetir esse determinado trecho de código)
#Lembrar da variável de controle -> define quando o loop irá para, sempre atualizar quando uma determinada condição foi atingida
#Sempre ter o passo -> quantas vezes vc irá executar essa condição

numero = 0

while numero <=100: #Se um número é menor ou igual a 100
    print(numero)
    numero += 1

#teste de mesa
#(rodada 1: numero =0
#           numero <= 100 => True
#           print(numero) => aparece 0 na tela
#           numero = numero + 1 (logo numero = 1))
#(rodada 2: numero =1
#           numero <= 100 => True
#           print(numero) => aparece 1 na tela
#           numero += 1 (logo numero = 2))
#.........
#(rodada 102: numero =101
#             numero <= 100 => False
#             sai do loop
#             print('fim do loop')
            
print('fim do loop')

#no While temo que:
#definiçãode varivel de controle
#block do while
#instruções do bloco
#adicionar uma instrução que modificasse a variável de controle