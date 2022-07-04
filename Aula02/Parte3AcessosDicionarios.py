#dicionários

dic = {
    'nome': 'Thais',
    'idade': 30,
    'dados': [0,1,2,3,4],
    'tupla': (0,1,2,3)
}

print(dic['tupla']) # (0,1,2,3)
print(dic['tupla'][-1]) #2

                #retorna ('nome, 'idade', 'dados', 'tuplas')
for chave in dic.keys():
    if chave == 'idade':
        print(f'achei -', dic[chave])
                #'Thais', 30, [0,1,2,3,4], (0,1,2,3)
for valor in dic.values():
    if valor == '30':
        print('achei a idade')
                #     'nome': 'Thais','idade': 30,'dados': [0,1,2,3,4],'tupla': (0,1,2,3)
for chave, valor in dic.items():
    print(f'key: {chave} - value: {valor}') #1: chave, valor = ('nome', 'Thais')

a,b,c =1 ,2,3  #associação paralela
print(f'a => {a}, b => {b}, c=> {c}') # a=1, b=2,c=3