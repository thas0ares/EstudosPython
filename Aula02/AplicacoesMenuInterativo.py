
while True:
    op = input('Digite a opção desejada:\n1- Saudação\n2- Sair\n3- Nenhuma das anteriores\n')

    if op == '1':
        print('uma saudação qualquer')
    elif op == '2':
        break #interrompe o loop
    elif op == '3':
        continue # pula para próxima rodada
    else:
        print('opção inválida')

print('fim')