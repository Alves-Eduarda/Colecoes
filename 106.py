c = ['\033[m',       # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m' # 6 - branco
     ]

def leia(msg, cor=0):
    t = len(msg) + 4
    print(c[cor], end='')
    print("="*t)
    print(msg)
    print("="*t)
    print(c[0], end='')


def ajuda(valor,cor =0):
    leia(f"Acessando o manual do comando \'{valor}\'", 4)
    print(c[6], end='')
    help(valor)
    print(c[0],end='')


while True:
    leia("  SISTEMA DE PYHELP  ", 2)
    n = str(input("Função ou Biblioteca => "))
    if n.upper() == "FIM":
        break
    else:
        ajuda(n)
leia(" ATÉ LOGO! ", 1)
