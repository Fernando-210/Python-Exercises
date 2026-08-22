from datetime import date
atual = date.today().year
nasc = int(input("ANO DE NASCIMENTO: "))
idade = atual - nasc
print (f"O atleta tem {idade} anos ")
if idade <= 25:
    print ("CLASSIFICAÇAO: MIRIM")
elif idade <=14:
    print ("CLASSIFICAÇAO: INFANTIL")
elif idade <=19:
    print ("CLASSIFICAÇAO: JUNIOR")
elif idade <=9:
    print ("CLASSIFICAÇAO: SENIOR")
else:
    print ("CLASSIFICAÇAO: MASTER")

