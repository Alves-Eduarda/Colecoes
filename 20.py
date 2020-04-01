from random import randint
mai = 0
list = []
print("Valores sorteados: ")
for c in range(1,5):
    jogador= randint(1,6)
    if c == 1:
        mai = jogador
    else:
        if jogador > mai:
            mai = jogador
    dic= {'njogador': c,'dado': jogador}
    print(f"O jogador{dic['njogador']} tirou {dic['dado']}")
    list.append(jogador)
    list.sort(reverse=True)
print("=-"*30)
print("Ranking dos jogadores: ")
for i, v in enumerate(list):
    print(f"{i+1}o. lugar : jogador{dic['njogador']} com {v}")
