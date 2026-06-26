print()
ano=int(input("Digite o ano: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("O ano é bissexto")
    print()
    print(f"Você digitou {ano}, este ano é bissexto")
    print("""""")
else:
    print("O ano não é bissexto")
    print()
    print(f"Você digitou {ano}, este ano não é bissexto")
    print("""""")