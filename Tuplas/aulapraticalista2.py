"""Lista dentro de listas
pessoas = [[ 'maria', 25], ['Joao', 45]]
lista = list()
lista.append('Gustavo')
lista.append(40)
print(lista)
galera = list()
# cria uma ligação entre as duas estruturas
# criando uma cópia onde as duas estruturas modificam ao mesmo tempo
galera.append(lista)
# criando uma estrutura onde as copias são independentes
galera.append(lista[:])
print(galera)
lista[0] = 'Maria'
lista[1] = 25
print(lista)
galera.append(lista[:])
print(galera)
"""
galera = [["Maria",25],["joao",12]]
for p in galera:
    print(p)
    print(f"nome {p[0]} , idade {p[1]}")