# São decisões em sequencias, e o motivo disso é a necessidade em e si de classificar em varias opções, voce tem várias opções
# e vc precisa decidir em qual caixinha essa informação se enquadra.

# Cálculo do IMC
### fórmula : peso(kg) / (altura ** 2)
# Intervalos :
# Baixo peso: < 18.5
# Peso Normal: 18.5 < peso < 24.9
# Pré Obesidade: 25.0 < 29.9
# Obesidade Grau I: 30.0 < 34.9
# Obesidade Grau II: 35.0 - 39.9
# Obesidade Grau III: > 40.0

# 1: Capturar as informações de peso e altura
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite o seu altura: '))

# 2: Calcular o índice do IMC
imc = peso / (altura ** 2)

# 3: Classificar o IMC
if imc < 18.5:
    print(f'Baixo peso - IMC: {imc:.2f}')
elif imc < 24.9:
    # {imc:.2f} -> Isso é uma delimitação de casas decimais
    print(f'Peso Normal - IMC: {imc:.2f}')
elif imc < 29.9:
    print(f'Pré Obesidade - IMC: {imc:.2f}')
elif imc < 34.9:
    print(f'Obesidade Grau I - IMC: {imc:.2f}')
elif imc < 39.9:
    print(f'Obesidade Grau II - IMC: {imc:.2f}')
else:  # se ele não caiu em nenhuma dessas aqui ele obrigatoriamente cai na última
    print(f'Obesidade Grau III - IMC: {imc:.2f}')
