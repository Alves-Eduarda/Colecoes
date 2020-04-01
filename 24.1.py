def traco ():
    print("=-"*25)


jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou ? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f" Quantos gols na partida {c}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        t = str(input("Deseja continuar [S/N]? ")).upper()
        if t not in "SN":
            print("ERRO! Responda apenas S ou N")
        else:
            break
    if t in "N":
        break
traco()
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
traco()
for k , v in enumerate(time):
    print(f'{k:>3}', end =' ')
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
traco()
while True:
    bus = int(input('Mostrar dados de qual jogador ? (999 para parar)'))
    if bus == 999:
        break
    if bus >= len(time):
        print(f"ERRO! Não existe jogador com código {bus}.")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[bus]['nome']}: ")
        for i, g in enumerate(time[bus]['gols']):
            print(f"   No jogo{i+1} fez {g} gols")
    traco()
print("VOLTE SEMPRE")
