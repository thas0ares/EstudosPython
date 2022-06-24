# instaciar um numero inteiro
inteiro = 15
# instaciar um texto
string = '15'
# função que inspeciona variáveis que vc definiu dentro do próprio interpretador
print(type(inteiro))  # retorna class 'int'
print(type(string))  # retorna class'str'
# números decimais, tem casas depois da vírgula com o ponto
decimal = 10.53
padrao_br = 10, 5
print(type(decimal))  # retorna class 'float'
print(type(padrao_br))  # retorna class 'tuple'
complexo = 5 + 5j  # tipo complexo
# retorna que é do tipo número e faz parte a class 'complex'
print(type(complexo))

# print(string + 10)  ---> não é possível realizar operações devido ao tipo de variável
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# Podemos realizar as operações de  +(soma) - (subtração) *(multiplicação) /(Divisão) **( exponenciação) // (Chão, divisão e ter como resultado sempre a parte inteiro, arredondando sempre para baixo ) % (resto da divsão)

num1 = 10
num2 = 3

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 ** num2)
print(num1 / num2)
# a ordem de resolução começa da direita para a esquerda
print(2 ** 3 ** 2)
print(2 ** 9)  # mesma resposta

print(4 / 2)
print(5 // 2)  # seria 2.5 porém utiliza o chão
print(5 % 2)
