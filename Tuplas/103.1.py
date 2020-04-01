def ficha(jog,gols):
    print(f"O jogador {jog} fez {gols} (s) no campeonato")


# Programa principal
n = str(input("Nome do jogador: "))
g = str(input("Número de gols : "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(jog="desconhecido",gols=g)
else:
    ficha(n,g)
