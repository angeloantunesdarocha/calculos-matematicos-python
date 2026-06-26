peso = float(input("Digite o peso do prato de comida: "))
preco = float(input("Digite o valor do 'KG' da comida:R$ "))
total = peso * preco
print()
print(f"Seu prato tem {peso:.3f}kg de comida")
print(f"O valor por quilo é: R${preco:.2f}")
print()
print(f"O valor total a pagar é: R${total:.2f}")
print()
