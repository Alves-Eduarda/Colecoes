temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input("Nome : ")))
    temp.append(float(input("Peso : ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1]> maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    c = str(input("Deseja continuar [S/N]? ")).upper()
    if c in "Nn":
        break
print("#"*45)
print(f"Ao todo você cadastrou {len(princ)} pessoas")
print(f"O maior peso foi de {maior} Kg. Peso de ", end="")
for p in princ:
    if p[1] == maior:
        print(f"{p[0]}")
print(f"O menor peso foi de {menor} Kg. Peso de ", end="")
for p in princ:
    if p[1] == menor:
        print(f"{p[0]}")
print()
