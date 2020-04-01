import random, time
jogo = []
temp = []
print("=-"*10, "MEGA SENA", "=-"*10)
n = int(input("Quantos jogos serão gerados ? "))
for c in range(1,n+1):
    for c in range(0,6):
        num = random.randint(1,60)
        temp.append(num)
    temp.sort()
    jogo.append(temp[:])
    temp.clear()
print("=-"*10,f"SORTEANDO {n} JOGOS","=-"*10)
for i , v in enumerate(jogo):
    time.sleep(1)
    print(f"jogo {i+1} : {v}")
print("=-"*14, "BOA SORTE","=-"*14)
