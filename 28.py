'''Dessa forma não consegui realizar a contagem do 0'''
from random import randint
def maior(*num):
    print("=-="*45)
    print("Analisando os valores passados...")
    for i, v in enumerate(num):
        print(f"{v} Foram informados {len(v)} valores ao todo.", end=" ")
        v.sort(reverse=True)
        print()
        print(f"O maior valor informado foi {v[0]}.")

def intervalo(i,f):
    for c in range(i,f):
        mai = randint(0,10)
        m.append(mai)
    maior(m)
    m.clear()

# principal
m = []
intervalo(0,6)
intervalo(0,3)
intervalo(0,2)
intervalo(0,1)
