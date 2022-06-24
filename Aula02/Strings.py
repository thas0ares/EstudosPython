from itertools import count


texto = '4 Linux Open Software Specialist'
print(type(texto))
outro_texto = "Isso também é aceitável no python"
frase = """
Isso é uma frase
permite wue você
escreva uma frase muito longa
mesma com caracteres especiais %$¨%$¨%$%¨$
e termina aqui
"""
print(frase)
# no retorno tempos um pulo de linha e \\n
caracteres_especiais = '\\n'
print(caracteres_especiais)  # retorna \n
caracteres_especiais = '\n'
print(caracteres_especiais)  # retorna o pulo da linha, vazio

print('\t isso é um tab')
print('\t\t isso é um tab')

print(texto)  # trabalhando com o Slince
print(texto[0])  # imprime o primeiro caracter da variavel texto ..
# pega do 0 até o 4, lembrando que o último número não está incluido)
print(texto[0:5])
print(texto[-1])  # pega o último valor
print(texto[0:10:-1])  # pega de forma reversa
print(texto[-1:0:-1])  # fazer o inverso da string, pulando de 1 em 1

# texto. mostra uma sequencia de funções que podem ser realizadas com a string, comportamentos associados as strings

print(texto.upper())  # Deixa em maiúsculas
print(texto.lower())  # Minúscula
print(texto.startswith('4'))  # começa com... retorna true
print(texto.startswith('4li'))  # retorna false
print(texto.endswith('t'))  # frase finaliza com .. retorna true

# retorna class 'bool' -> tipo booleano o True ou False... são utilizados com letras maiúsculas
print(type(texto.endswith('t')))

texto.split()  # utilizado em lista, ele consegue separar minha frase em unidades individuais de txt em por alguma caractere especial, nesse caso ele esta utilizando o espaço
texto_separo_por_virgulas = 'nome,idade,sexo,cpf,uf'
# retorna ['nome', 'idade', 'sexo', 'cpf', 'uf'] esse tipo de dado é uma lista, uma outra forma de interpretação de txt
print(texto_separo_por_virgulas.split(','))

help(texto.count)  # retorna uma descrição do que aquele comportamento faz

print(texto.count('Open'))  # conta quantos Open existem
print(texto.count('u', 0, 6))  # conta as letras 'u' de 0  á 6

outro_texto = 'conteudo de texto     '
print(outro_texto.strip())  # trata essses espaços vazios
