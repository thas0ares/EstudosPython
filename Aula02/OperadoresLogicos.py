# Operadores lógicos -> And, or, not

texto = 'um texto qualquer'
pula_linha = '\n'
print(texto.endswith('um'))
# o que é feito por baixo dos panos ==> 'um' and 'um' - ele retorna True
print(texto.startswith('um'))

print(5 > 5)  # False
print(5 >= 5)  # True

print(pula_linha)

# resolve cada bloco separo e apos compara os resultados para ver se a resolução é verdadeira
# AND//E
# True and True ==> True (só retorna true se ambas as preposições forem verdadeiras)
print((5 >= 5) and (4 > 3))
print((5 >= 5) and (4 < 3))  # True and False => False
print((5 > 5) and (4 > 3))  # False and True => False
print((5 > 5) and (4 < 3))  # False and False => False


print(pula_linha)

# OR//OU
print((5 >= 5) or (4 > 3))  # True or True ==> True
print((5 >= 5) or (4 < 3))  # True or False => True
print((5 > 5) or (4 > 3))  # False or True => True
print((5 > 5) or (4 < 3))  # False or False => False

print(pula_linha)

# NOT//NÃO
print(5 > 5)  # retorna False
# porém é uma forma de negar
print(not 5 > 5)  # agora retornou True

print(pula_linha)

# Igualdade
print(5 == 5)  # retorna True
print('esse texto' != 'outro texto')  # != diferente
