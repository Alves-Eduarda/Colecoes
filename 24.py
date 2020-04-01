lista = []
l = 0
while True:
    print("=-"*30)
    nome = str(input("Nome do jogador : "))
    part = int(input("Quantas partidas foram jogadas ? "))
    tot = 0
    gols = []
    dic = {'nome': nome, 'partidas': part, 'gols':gols, 'total': tot}
    for c in range (0,part):
        q = int(input(f"Quantos gols foram feitos na partida {c}? "))
        gols.append(q)
        tot+=q
        dic['total'] = tot
    lista.append(dic)
    t = str(input("Deseja continuar [S/N]? ")).upper()
    if t in "N":
        break
print("-=-"*20)
print(f"{'cod':<4}{'nome':>10}{'gols':>10}{'total':>10}")
print("-=-"*20)
for i,v in enumerate(lista):
    print(f"{i:<4} {lista[i]['nome']:>10} {lista[i]['gols']} {lista[i]['total']}", end='')
