def fatorial(n = 0,show=0):
    """
    ==> Calcula o fatorial de um número
    :param n: número que será calculado o fatorial
    :param show: valor lógico opcional, mostrar ou não a conta
    :return: devolve o valor do fatorial
    """
    f = 1
    print("=-=" * 20)
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(f" x ", end=" ")
            else:
                print(f' = ', end='')
    return f


#Programa principal
print(fatorial(5,show=True))
