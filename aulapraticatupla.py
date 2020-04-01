lanche = ('Hambúrguer','Pizza','Guaraná')
#mostra a posição de cada repetição
for c in range(0,len(lanche)):
    print(lanche[c])

# não mostra a posição
for c in lanche:
    print(c)

for pos,c in enumerate(lanche):
    print(f"Eu vou comer {c} na posição {pos} ")

# uso do sorted - mostra em ordem
print(sorted(lanche))

# manipulação de duas tuplas
# o uso do + junta duas tuplas, cuidado com a ordem
a = (2,3,4,2)
b =(5,6,7)
c = a +b
print(c)

# metodos na tupla
# mostra quantas vezes aparece o número indicado
print(c.count(9))
# mostra qual é a posição do número indicado na tupla, pegando da primeira posição
print(c.index(6))
# deslocamento - mostra o número a partir da posição escolhida no segundo valor
print(c.index(2,1))

#podem existir dados de um tipo diferente dentro da tupla

# uso do del - deleta a tupla inteira, não tem como apagar apenas um elemento da tupla
del(c)
