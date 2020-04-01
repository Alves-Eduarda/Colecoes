def ficha(j='', g=' '):
    if j == '' and g == '':
        print(f"O jogador desconhecido fez 0 gol (s) no campeonato. ")
    elif j == '':
        print(f"O jogador desconhecido fez {g} gol (s) no campeonato. ")
    elif g == '':
        print(f"O jogador {j} fez 0 gol (s) no campeonato. ")
    else:
        print(f"O jogador {j} fez {g} gol (s) no campeonato.")


print("=-="*15)
jogador = str(input("Nome do jogador : "))
gols = str(input("Número de gols : "))
ficha(jogador,gols)
