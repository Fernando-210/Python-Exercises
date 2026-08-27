maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f"Peso da {p}ª Pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print (f"O maior peso foi {maior}Kg")
print (f"E o menor peso foi {menor}Kg")
