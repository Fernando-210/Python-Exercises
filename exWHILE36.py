print ("-"*15)
print("LOJA SUPER LIDL")
print ("-"*15)
total= cont = menor = totmil =0
barato = " "
while True:
    np = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = np 
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? ")).upper().split()[0]
    if resp == "N":
        break
print ("FIM DO PROGRAMA")
print (f"O total da compra deu R${total:.2f}")
print (f"Temos {totmil} produtos custando mais de R$1000")
print (f"O produto mais barato foi {barato} que custa R${menor:.2f}")
