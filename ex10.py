print ("{:=^40}".format("BEM VINDO AO LIDL"))
preço = float(input("Preço das compras: "))
print (""" Formas de pagamento
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opçao = int(input("Qual é a opçao? "))
if opçao == 1:
    total = preço - (preço * 10/100)
elif opçao == 2:
    total = preço - (preço * 5/100)
elif opçao == 3:
    total = preço 
    parcela = total / 2
    print (f"Sua compra sera parcelada em 2x de R${parcela:.2f} ")
elif opçao == 4:
    total = preço + (preço * 20/100)
    totalP = int(input("Quantas parcelas: "))
    parcela = total / totalP
    print (f"sua compra sera parcela em {totalP} vezes de {parcela:.2f}")
else: 
    total = preço
    print("OPÇAO INVALIDA DE PAGAMENTO. POR FAVOR TENTE NOVAMENTE")
print (f"Sua compra de R${preço:.2f} vai custar um toal de R${total:.2f} no final ")
