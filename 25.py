def area(a,b):
    print(f"A área do terreno de {a:.1f} m x {b:.1f} m = {a*b:5.1f} m² ")

def mostralinha():
    print("=-="*10)
    print(" >> CONTROLE DE TERRENO << ")
    print("=-="*10)
mostralinha()
a = float(input("Informe a largura do terreno (em metros) : "))
b = float(input("Informe o comprimento do terreno (em metros) : "))
area(a,b)
