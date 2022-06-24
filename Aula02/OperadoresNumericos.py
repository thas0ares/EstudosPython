# Opeções com string

texto = 'um texto qualquer'
outro_texto = '10'
print(texto * 10)  # ele repete 10 vezes
# ele junta os txt, faz uma concatenação (lembrando que não se concatena, string com inteiro)
print(texto + outro_texto)
# no caso de txt com txt e divisão também não são aceitáveis

contador = 0
contador = contador + 1
print(contador)
contador = contador + 1  # acumular
print(contador)

# com outra notação
contador += 1
print(contador)

contador *= 2  # com multiplicação
print(contador)

contador /= 2  # vcom divisão, sendo que o tipo modifica para un tipo flutuante -> float
print(contador)
