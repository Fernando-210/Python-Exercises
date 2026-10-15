maior=menor=0
for p in range(1,8):
    peso= float(input("Peso dA {p} pessoa"))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de {maior}kg")
print(f"O maior peso lido foi de {menor}kg")
