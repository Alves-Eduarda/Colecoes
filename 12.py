texto = str(input("Digite uma frase : "))
pilha = []
for simb in texto:
  if simb == "(":
      pilha.append("(")
  elif simb == ")":
      if len(pilha) > 0:
          pilha.pop()
      else:
          pilha.append(")")
          break
if len(pilha) == 0:
    print("Sua expresão está válida")
else:
    print("Sua expressão não está válida")
