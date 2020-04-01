lista = []
listapar =[]
listaimpar= []
while True:
    lista.append(int(input("Digite um valor : ")))
    t = str(input("Deseja continuar [S/N] ? ")).upper()
    while t not in "nNsS":
        t = str(input("Favor, deseja continuar [S/N] ? ")).upper()
    if t == "N":
        break
for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print("=*"*30)
print(f"A lista de valores gerados foi {lista}")
print(f"A lista de valores pares foi {listapar}")
print(f"A lista de valores ímpares foi {listaimpar}")