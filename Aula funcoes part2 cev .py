'''
#Docstring

def contador(i,f,p):
    """
        -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
        -> Função criada por duda :)
    """
    c=i
    while c<= f:
        print(f"{c}", end="..")
        c+= p
    print('FIM!')


contador(0,10,2)
help(contador)

#parametros adicionais

def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3,2,5)
somar(8,4)
somar()

# escopo de variáveis
def teste():
    x = 9
    print(f"Na função teste, x vale {x}")
    print(f"Na função teste, x vale {n}")


#Programa Principal
n = 2
print(f'No programa principal, x vale {n}')
teste()
def funcao():
    n1 = 4
    print(f"N1 dentro vale {n1}")


n1 = 2
print(f"N1 global vale {n1}")
funcao()

print()
def teste(b):
# aqui não tenho um a local criado
    global a
    a = 8
    b+= 4
    c =2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a = 5
teste(a)
print(f"A fora vale {a}")

# retornando valores
def somar(a=0,b=0,c=0):
    s = a+b+c
    return s


resp = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f"Meus cálculos deram {resp} , {r2} e  {r3}.")


def fatorial(num):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(3)
f3= fatorial(6)
print(f"O resultado é {f1} {f2} e {f3} ")

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

n1 = par(2)
print(n1)
'''


