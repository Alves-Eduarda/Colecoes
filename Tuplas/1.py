numeros = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezesete","dezoito","dezenove","vinte")
n = int(input("Digite um número entre 0 e 20 : "))
while True:
    if n > 20 or n < 0:
        print("Você digitou um número incorreto. Tente novamente.")
        n = int(input("Digite um número entre 0 e 20 : "))
    else:
        break

print("Voce digitou o número", numeros[n])
