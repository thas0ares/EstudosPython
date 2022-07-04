#é realizado uma busca direto pela palavra
#é uma forma de vc armazenar mais de uma informação, que o acesso que vc tenha é pela palavra chave
#vc pode acessar o conteúde se vc souber a chave
#utilizamos as chaves  {}
#ele deriva de JSON, é um dicionario 

dicionario = {}
print(type(dicionario))

#help({})

dicionario['nome'] = 'Thais Soares Alves da Silva Rossi'
print(dicionario)
print(dicionario['nome'])

#aceitam outros dados, e é uma forma de armazenamento de dados por chave e valor
dicionario['idade'] = 32
print(dicionario)
print(dicionario['idade'])

#dicionario. -> não tem informação pra adicionar, em um dicionario é feito de forma direta mesmo
dicionario['chave'] = 'valor desejado'
print(dicionario)

#para remover, do mesmo jeito que em lista
del dicionario['chave']
print(dicionario)


#inspecionar chaver dentro, retorna lista com nomes das chaves que estão armazenadas dentro do dicionario
print(dicionario.keys())

#pegar os valores
print(dicionario.values())

#acessar uma informação do dicionario
print(dicionario['nome']) #dá um erro
print(dicionario.get('idade')) #o get esta guardando a informação a chave que quero acessar, ele tem um segurança se a chave não existir ele retorna um valor vazio um 'none'

#outra forma de remover
print(dicionario.pop('nome')) # achar o que vc quer remover, retornar o que removou e por fim deletar da estrutura
print(dicionario)


