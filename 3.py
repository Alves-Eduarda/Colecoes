from random import randint
menor = maior = 0
n1 = (randint(0,100), randint(0,100) , randint(0,100) , randint(0,100) ,randint(0,100))
numeros = (n1)
print("Os números gerados foram : ", numeros)
maior = sorted(numeros)
print("O maior número foi : ", maior[4])
print("O menor número foi : ", maior[0])
