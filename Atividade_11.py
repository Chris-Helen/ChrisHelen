a = int(input("Digite um número: "))
if (a % 2 == 0):
    if (a > 0):
        print("Par positivo")
    elif (a < 0):
        print("Par negativo")
    else:
        print("Par positivo")
else:
    print("Ímpar")