lista = list ()
while True:
    d = int(input("Digite um valor : "))
    if d not in lista:
        lista.append(d)
        print("Valor adicionado com sucesso....")
    else:
        print("Valor duplicado, não vou adicionar....")
    t = str(input("Deseja continuar [S/N] ? ")).upper()
    while t not in "SsNn":
        t = str(input("Favor, informe se deseja continuar [S/N] : ")).upper()
    if t == "N":
        break
lista.sort()
print("=*"*30)
print(f"Você digitou os valores {lista}")