matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somac = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
        if matriz[l][c] %2 ==0:
            soma +=matriz[l][c]
print("=-" * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()
print("=-"*30)
print(f"A soma dos valores pares foi : {soma}")
for l in range (0,3):
    somac += matriz[l][2]
print(f"A soma dos valores da terceira coluna foi : {somac}")
for c in range (0,3):
    if c == 0 :
        mai = matriz[1][c]
    else:
        mai = matriz[1][c]
print(f"O maior valor da segunda linha é : {mai}")
