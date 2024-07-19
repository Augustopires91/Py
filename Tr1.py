print("Sou Augusto Vallez")
ValordoPedido = float(input('Valor do pedido:'))
QuantidadeDeParcelas = int(input('Quantidade de Parcelas:'))

if QuantidadeDeParcelas<4:
    juros = 0

elif 4<=QuantidadeDeParcelas<6:
    juros = 4/100

elif 6<=QuantidadeDeParcelas<9:
    juros = 8/100

elif 9<=QuantidadeDeParcelas<13:
    juros = 16/100

elif QuantidadeDeParcelas>=13:
    juros = 32/100

else: print('valor invalido')


valordaparcela = (ValordoPedido*(1+juros))/QuantidadeDeParcelas

valortotalparcelado = valordaparcela*QuantidadeDeParcelas

print('Valor das Parcelas: R$ {:.2f}'.format(valordaparcela))
print('Valor Total Parcelado: R$ {:.2f}'.format(valortotalparcelado))
