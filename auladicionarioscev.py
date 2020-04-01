"""pessoas = {'nome': 'Gustavo', 'Sexo':'M','idade':22}
print(pessoas)
print(pessoas['nome'])
# Na hora de referenciar os elementos usa-se colchetes, na hora de declarar um elemento usa-se chaves
# se eu colocar aspas simples no print formatado, preciso colocar dentro da referência aspas duplas quando for chamar esse elemento
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos ')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
#removendo
del pessoas['Sexo']
#trocando a variável
pessoas['nome'] = 'Leandro'
#adicionando
pessoas['peso'] = 90
for k, v in pessoas.items():
    print(f'{k} = {v}')
#criando dicionários dentro de uma lista
estado = {'UF': 'Rio de Janeiro', 'Sigla' : 'RJ'}
estado1 = {'UF': 'São Paulo','Sigla' : 'SP'}
lista =[]
lista.append(estado)
lista.append(estado1)
print(lista)
print(lista[0]['Sigla'])"""
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
#para cada estado em brasil mostre o estado, indices 0,1 e 2
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

# retorna somente os valores
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
