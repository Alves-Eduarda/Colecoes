from random import randint
# presença do parâmetro n
def sorteia(n):
    numeros.append(n)

# função sem parâmetro
def somapar():
    soma = 0
    for i,v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(soma)

def linha():
    print("=-="*30)
numeros = []
for c in range(0,5):
    sorteia(randint(0,100))
linha()
print(f"Os números que fazem parte da lista são : {numeros}")
linha()
print(f"A soma dos números pares é :", end=' ')
somapar()
linha()
