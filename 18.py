from time import sleep
temp = []
princ = []
while True:
    temp.append(str(input("Nome do aluno :")))
    temp.append(float(input("Informe a primeira nota : ")))
    temp.append(float(input("Informe a segunda nota : ")))
    temp.append((temp[1] + temp[2])/2)
    princ.append(temp[:])
    temp.clear()
    t = str(input("Deseja continuar [S/N] ? ")).upper()
    if t in "N":
        break
print("="*20, "< BOLETIM >","="*20)
print(f"{'No.':<4}{'Nome':^10}{'Média':>8}")
print("="*50)
for p, w in enumerate(princ):
    print(f"{p:<4}{w[0]:^10}{w[3]:>8.2f}")
print("="*50)
while True:
    f = int(input("Mostrar notas de qual aluno ?(999 interromper) "))
    for j, u in enumerate(princ) :
        if f == j:
            print(f"Notas de {u[0]} são {u[1],u[2]}")
    if f == 999:
        break
sleep(1)
print("="*10,"FINALIZANDO","="*10)
