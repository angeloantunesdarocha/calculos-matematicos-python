import math

numero = float(input("Digite um número para calcular a raiz quadrada: "))

if numero < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
else:
    resultado = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {resultado}")
