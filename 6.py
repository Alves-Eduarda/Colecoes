palavras = 'Python','Marcelo','Televisao','hugo'
for c in palavras:
    print(f"\nNa palavra {c.upper()} temos ",end="")
    for letra in c:
        if letra.lower() in "aeiou":
            print(f"{letra}", end=" ")
