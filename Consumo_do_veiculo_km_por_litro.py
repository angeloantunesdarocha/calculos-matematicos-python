distancia = float(input("Quantos KM percorridos? "))
litros = float(input("Quantos litros de combustível gasto? "))
preco = float(input("Quanto custa cada litro de combustível? "))
print()
div = distancia / litros
multiplica = litros * preco
print(
    f"Você percorreu {distancia} quilômetros\nCom {litros} litros de combustível\nVocê gastou R${multiplica:.2f} de combustível\nSeu carro fez {div:.2f} quilômetros por litro!"
)
