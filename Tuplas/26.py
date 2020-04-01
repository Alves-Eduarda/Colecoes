def escreva(t):
    print("~" * t)

lista = []
p = '>> CURSO EM VÍDEO <<'
lista.append(p)
m = ' Curso de Python no Youtube '
lista.append(m)
j = ' CeV '
lista.append(j)
for i, v in enumerate(lista):
    escreva(len(v))
    print(f"{v}")
    escreva(len(v))


