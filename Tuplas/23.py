lista = []
somaidade = 0
while True:
    nome = str(input("Nome : "))
    sexo = str(input("Sexo [F/M] : ")).upper()
    while sexo not in "FM":
        print("Por favor, digite apenas M ou F.")
        sexo = str(input("Sexo [F/M] : ")).upper()
    idade = int(input("Idade : "))
    somaidade += idade
    dict = {'nome': nome, 'sexo' : sexo, 'idade': idade}
    lista.append(dict.copy())
    t = str(input("Deseja continuar [S/N] ? ")).upper()
    while t not in "SsNn":
        print("ERRO! Por favor, digite apenas S ou N.")
        t = str(input("Deseja continuar [S/N] ? ")).upper()
    if t in "N":
        break
print("=-="*20)
print(f"A) Foram cadastradas {len(lista)} pessoas")
media = (somaidade)/len(lista)
#5.2 - cinco casas ao todo e 2 casas decimais
print(f"B) A média de idade do grupo : {media:5.2f}")
print(f"C) As mulheres cadastradas : ", end=" ")
for i, v in enumerate(lista):
    if lista[i]['sexo'] == 'F':
        print(f"{lista[i]['nome']}", end=" ")
print()
print(f"D) As pessoas com a idade acima da média : ")
for i,v  in enumerate(lista):
    if lista[i]['idade'] > media:
       print(f'  nome = {lista[i]["nome"]};', end='')
       print(f'  sexo = {lista[i]["sexo"]};', end='')
       print(f'  idade = {lista[i]["idade"]};')
print("<< ENCERRADO >>")
