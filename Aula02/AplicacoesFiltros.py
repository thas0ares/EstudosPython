texto= """

O rato roeu a roupa do rei de Roma

"""

#Quantas vezes aparecem as vogais no texto?
vogal = 0

for caractere in texto:
    if caractere.lower() in 'aeiou':
        vogal += 1

print('total de vogais: {}'.format(vogal))

#Qual o número de vezes que a consoante R aparece no texto?

erres=0

for caractere in texto:
    if 'r' in caractere.lower():
        erres +=1
print('O texto possui {} caracteres \'r\' '. format(erres))








exit()  #ignora todos os comando wque estiverem para baixo, só vale o que estiver acima
##Lista de compras
lista_de_compras = [
    ('Camiseta', 19.90),
    ('Calca Jeans', 20.50),
    ('Meias G', 5.90),
    ('Camiseta M', 10.00),
    ('CAMISETA', 10.00)
]

#probelma: totalizar o carrinho de compras aplicando 10% de desconto ao item 'Camiseta'

total = 0
desconto = 0.9

for compra in lista_de_compras:
    if compra[0].upper() == 'CAMISETA':
        total += compra[1] * desconto
    elif 'camiseta' in compra[0].lower():
        total += compra[1] * desconto
    else:
        total += compra[1]
print(f'Valor total de compras aplicando o desconto: {total:.2f}')