''' desempacotamento de funções
def contador(*num):
cont = 0
for i , v in enumerate (num):
    cont += num[i]
print(f"{cont}", end="")
print("FIM")

contador (1,2,3,4)
contador (4,2)'''

''' Uso de listas nas funções
def dobra(lst):
pos = 0
while pos < len(lst):
    lst[pos] *= 2
    pos += 1


lista = [1,2,3,45]
dobra(lista)
print(lista)'''

'''def cantar_parabens():
    print("Parabéns para Você!")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida!")


cantar_parabens()
# retornando uma função

def diz_oi():
    print("Estou sendo executado antes do retorno....")
    return 'OI!'
print(diz_oi())

'''
'''from random import random
def joga_moeda():
    valor = random()
    # gera números reais entre 0 e 1
    print(valor)
    if valor > 0.5:
        return "Cara"
    # posso omitir o else
    return "Coroa"
    
    
print(joga_moeda())
'''







