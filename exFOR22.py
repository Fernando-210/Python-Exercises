somaidade = 0
medidade = 0
midadeh = 0
nvelho = " "
totmulher20 = 0
for p in range(1,5):
    print(f"===={p}ª Pessoa ====")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        midadeh = idade
        nvelho = nome
    if sexo in "Mm" and idade > midadeh:
        midadeh = idade
        nvelho = nome
    if sexo in "Ff" and idade <20:
        totmulher20 += 1 
medidade = somaidade / 4
print (f"A media de idade o grupo é e {medidade} anos")
print (f"O homem mais velho tem {midadeh} anos e se chama {nvelho}")
print (f"Ao todo sao {totmulher20} mulheres com menos de 20 anos ")
