matriz = [[],[],[]]
soma = maior = somac = menor = 0
for c in range(0,3):
    num = int(input(f"Digite um valor para {[0,c]}: "))
    matriz[0].append(num)
    if num % 2 ==0:
        soma+=num
for c in range(0,3):
    num = int(input(f"Digite um valor para {[1, c]}: "))
    matriz[1].append(num)
    if num % 2 == 0:
        soma += num
    if c == 0 :
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor :
            menor = num
for c in range(0,3):
    num = int(input(f"Digite um valor para {[2, c]}: "))
    matriz[2].append(num)
    if num % 2 == 0:
        soma += num
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
print(f"A soma dos valores pares é : {soma}")
c1 = matriz[0][2]
c2 = matriz[1][2]
c3 = matriz[2][2]
somac = c1 + c2 + c3
print(f"A soma dos valores da terceira coluna : {somac}")
print(f"O maior valor da segunda linha : {maior}")
