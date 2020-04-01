nome = str(input("Nome: "))
media = float(input(f"Média de {nome} : "))
nota = {'nome': nome,'media': media}
print("=-"*30)
print(f"Nome é igual a {nota['nome']}")
print(f"Média igual a {nota['media']}")
if nota['media'] >= 7 :
    print("Aprovado")
elif 5 <= nota['media'] < 7:
    print('Em recuperação')
else:
    print("Reprovado")
