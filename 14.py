listapar = []
listaimpar = []
lista = []
for c in range(1,8):
    n = int(input(f"Digite o {c}o valor : "))
    if n % 2 ==0:
        listapar.append(n)
    else:
        listaimpar.append(n)
listapar.sort()
listaimpar.sort()
lista.append(listapar[:])
lista.append(listaimpar[:])
print("=!"*40)
print(f"Os valores pares digitados foram : {lista[0]}")
print(f"Os valores ímpares digitados foram : {lista[1]}")
