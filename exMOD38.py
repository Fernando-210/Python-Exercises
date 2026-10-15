resp = "S"
soma = quant = maior = menor = media = 0
while resp in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    quant += 1
    if quant == 1:
        menor = maior = num
    
    resp = str(input("Quer continuar? [S/N]"))
print (f"Voce digitou {quant} numeros e a media foi {media}")
print (f"O maior valor foi {maior} e o menor valor foi {menor}")
