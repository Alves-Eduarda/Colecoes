from time import sleep


def maior(*num):
    print("=-=" * 45)
    print("Analisando os valores passados...")
    mai  = 0
    for n in num:
        print(f"{n} ", end=' ')
        sleep(0.3)
    print(f"Foram analisados {len(num)} valores ao todo.")
    for d in num:
        if mai == 0:
            mai = d
        else:
            if d > mai:
                mai = d
    print(f"O maior valor informado foi {mai}.")


# Programa principal
maior(2,8,9,2,5,7)
maior(4,7,0)
maior(1,2)
maior(6)
maior()