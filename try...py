# titulo
print("Camisetas Augusto M Vallez")

print("\n")

# Menu dos modelos
print("Escolha o modelo:")
print ("MCS - Camiseta Manga Curta Simples")
print ("MLS - Camiseta Manga Longa Simples")
print ("MCE - Camiseta Manga Curta Escondida")
print ("MLE - Camiseta Manga Longa Escondida")

# Função para escolher o modelo
def escolha_modelo():
  while True:
    modelo = input(">>")
    if modelo in ["MCS", "MLS", "MCE", "MLE"]:
      return modelo
    else:
      print("Modelo inválido. Tente novamente.")

modelo = escolha_modelo()# Chama a função para escolher o modelo

print("\n")

# Define o preço unitario 
if modelo == "MCS":
    preco_unitario = 1.80
elif modelo == "MLS":
    preco_unitario = 2.10
elif modelo == "MCE":
    preco_unitario = 2.90
elif modelo == "MLE":
    preco_unitario = 3.20

preco_base = preco_unitario

# Função para calcular o numero de camisetas com desconto
def num_camisetas():
  while True:
    try:
      num = int(input("Digite o número de camisetas: "))
      if num > 0 and num <= 20000:
        if num < 20:
          desconto = 0
        elif num >= 20 and num < 200:
          desconto = num * 0.05
        elif num >= 200 and num < 2000:
          desconto = num * 0.07
        elif num >= 2000 and num <= 20000:
          desconto = num * 0.12
        return round(num - desconto)# Retornoa o número de camisetas com desconto
      else:
        print("Número inválido. Digite um número entre 1 e 20000.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")

num_camisetas_com_desconto = num_camisetas()
print("\n")

print("Escolha o tipo de frete:")# Menu de opções de frete
print("1 - Transportadora = R$ 100,00")
print("2 - Sedex = R$ 200,00")
print("0 - retirar na Loja = R$ 0.00")

def frete():# Função para escolher o frete
    while True:
      try:
          frete = input(">>")
          if frete == '1':
            return 100.00 
          elif frete == '2':
            return 200.00
          elif frete == '0':
           return None
          else:
             print("Opção inválida. Digite 1, 2 ou 0.")
      except:
        print("Entrada inválida.")

valor_frete = frete()

# funçoes para calcular o frete
if valor_frete is not None:
    preco_total = preco_base + valor_frete
else:
    preco_total = preco_base

# Calcula o preço total
preco_total = num_camisetas_com_desconto * preco_unitario + valor_frete

print("\n")

# Mostra o Preço total Com detalhes
print(f"total: R$ {preco_total:.2f} (Modelo: {modelo} = {preco_unitario:.2f} * Quantidade (com desconto): {num_camisetas_com_desconto} + frete: R$ {valor_frete:.2f})")
