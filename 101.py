def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos : VOTO OPCIONAL."
    elif idade < 16:
        return f"Com {idade} anos : NÃO VOTA."
    else:
        return f"Com {idade} anos : VOTO OBRIGATÓRIO."


#programa principal
print("=-"*30)
n = int(input('Em que ano voce nasceu ? '))
print(voto(n))
