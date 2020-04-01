'''listas6 = [1,2,3,True,'Geek',[1,2,3]]
print(listas6)
print(type(listas6))
for elemento in listas6:
    print(elemento)'''

carrinho = []
while True:
    produto = str(input("Adicione um produto (digite sair para sair) : ")).lower()
    if produto != 'sair':
        carrinho.append(produto)
    else:
        break
for produto in carrinho:
    print(produto)
