print("=!"*30)
print(f'{"LISTA DE COMPRAS":^60}')
print("=!"*30)
lista = 'Guaraná',3.50 , "UVA", 2 , "Biscoito", 3.20 , "Suco", 4
for pos in range(0,len(lista)):
    if pos %  2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:<7.2f}')
print("=!"*30)

