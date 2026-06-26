primeiro_valor=float(input("Digite o primeiro valor: "))
segundo_valor=float(input("Digite o segundo valor: "))
terceiro_valor=float(input("Digite o terceiro valor: "))
print()
if primeiro_valor==segundo_valor and segundo_valor==terceiro_valor:
    print()
    print("Os três valores formam um triângulo equilátero.")
    print()
elif primeiro_valor==segundo_valor or segundo_valor==terceiro_valor or terceiro_valor==primeiro_valor:
    print()
    print("Os três valores formam um triângulo isósceles.")
    print()
else:
    print()
    print("Os três valores formam um triângulo escaleno.")
    print()

