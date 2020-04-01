lista = []
for c in range (1,6):
    lista.append(int(input(f"Digite o {c} valor : ")))
nova = lista.copy()
nova.sort()
maior = nova[-1]
menor = nova[0]
print("~"*50)
print(f"Você digitou os números : {lista}")
print(f"O maior valor digitado foi {maior}, nas posições ", end=" ")
for i,v in enumerate(lista):
    if v == maior:
        print(f"{i + 1}...", end= " ")
print()
print(f"O menor valor digitado foi {menor}, nas posições ", end="")
for i,v in enumerate(lista):
    if v == menor:
        print(f"{i + 1}...", end= "")
print()