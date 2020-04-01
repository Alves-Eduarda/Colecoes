num = [[],[]]
for c in range (1,8):
    n = int(input(f"Digite o {c}o valor :"))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print("=!"*40)
print(f"Os números pares digitados foram : {num[0]}")
print(f"Os números ímpares digitados foram : {num[1]}")
