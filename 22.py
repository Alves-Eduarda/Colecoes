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
print("-=-"*20)
print(dic)
print("-=-"*20)
for k,v in dic.items():
    print(f"O campo {k} tem o valor {v}")
print("-=-"*20)
print(f"O jogador {dic['nome']} jogou {dic['partidas']} partidas.")
for i, v in enumerate(dic['gols']):
    print(f"   => Na partida {i}, fez {v} gols.")
print(f"Foi um total de {dic['total']} gols.")
