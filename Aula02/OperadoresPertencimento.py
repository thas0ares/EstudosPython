# utilizado quando queremos comparar textos ou se um elemento pertence ou esta contido em um conjunto de elementos, validar algum conjunto de caracteres
texto = 'um texto qualquer'

# verifico se texto está contido na variavel texto, retorna True
print('qualquer' in texto)

print('oi' in texto)  # retorna False

# combinar operações lógicas, esse conjuto de caracteres não esta no texto  retorna True
print('oi' not in texto)

# pensando em tuplas
print(texto.split())  # ele separa o conjunto de elementos
print('um' in texto.split())  # valida retornando um True
