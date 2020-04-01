matriz = [[],[],[]]
for c in range(0,3):
    num = int(input(f"Digite um valor para {[0,c]}: "))
    matriz[0].append(num)
for c in range(0,3):
    num = int(input(f"Digite um valor para {[1, c]}: "))
    matriz[1].append(num)
for c in range(0,3):
    num = int(input(f"Digite um valor para {[2, c]}: "))
    matriz[2].append(num)
print("=-"*40)
for p in matriz[0]:
    print("[",p,"]", end=" ")
print()
for p in matriz[1]:
    print("[", p, "]", end= " ")
print()
for p in matriz[2]:
    print("[", p, "]", end= " ")
print()
