from datetime import date
nome = str(input("Nome : "))
ano = int(input("Ano de nascimento : "))
anoatual = date.today()
idade = anoatual.year - ano
carteira = int(input("Caretira de trabalho (0 não tem) : "))
dic = {'nome' : nome, 'idade': idade ,'ctps': carteira}
if carteira != 0:
    contrato = int(input("Ano de contratação : "))
    dic['contratação'] = contrato
    aposentadoria = 35 + contrato
    sal = float(input("Salário : R$ "))
    dic['salario'] = sal
    dic['aposentadoria'] = idade + (aposentadoria - anoatual.year)
print("=-"*40)
for k, v in dic.items():
    if k not in 'ano':
        print(f"-- {k} tem o valor {v}")
