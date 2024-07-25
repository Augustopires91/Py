# Nome completo e Menu (Cardápio)
print("Marmitas Augusto M Vallez") 

print("|---------------------------- Cardápio ----------------------------|")
print("|--| Tamanho |--| Bife Acebolado (BA) |--|  Filé de Frango (FF) |--|")
print("|--|    P    |--|      R$ 16.00       |--|       R$ 15.00       |--|")
print("|--|    M    |--|      R$ 18.00       |--|       R$ 17.00       |--|")
print("|--|    G    |--|      R$ 22.00       |--|       R$ 21.00       |--|")
print("|------------------------------------------------------------------|")
total = 0

# Inicio do loop 

while True:
    sabor = input("Escolha o sabor do Dia (BA/FF): ")

    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente.")
        continue

    tamanho = input("Escolha o tamanho que deseja (P/M/G): ")

    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue

# Calculo do Preço de acordo com as escolhas

    if sabor == "BA":
        if tamanho == "P":
            preco = 16
        elif tamanho == "M":
            preco = 18
        else:
            preco = 22
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15
        elif tamanho == "M":
            preco = 17
        else:
            preco = 21

    total += preco
    print("Preço do pedido: R$", preco)

# Dá continuidade no pedido

    mais = input("Deseja pedir mais alguma coisa? (S/N): ")
    if mais.upper() != "S":
        break # encerra o programa
# imprime o total do pedido
print("Valor total do pedido: R$", total)