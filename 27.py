def contador(conta):
    print(f"{conta}",end= " ")

def linha():
    print("=-="*20)
linha()
print(f"{'Contando de 1 até 10 de 1 em 1    '}")
for c in range(1,11,1):
    contador(c)
print("FIM!")
linha()
print(f"Contando de 10 até 0 de 2 em 2    ")
for a in range(10,-2,-2):
    contador(a)
print("FIM!")
linha()
print('Agora é sua vez de personalizar a contagem!')
n1 = int(input("Início : "))
n2 = int(input("Final : "))
p = int(input("Passo : "))
linha()
for c in range(n1,n2+p,p):
    contador(c)
print("FIM!")
