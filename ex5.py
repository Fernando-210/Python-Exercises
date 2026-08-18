from datetime import date
atual = date.today().year
nasc = int(input("Em que ano voce nasceu: "))
idade = atual - nasc
print (f"Quem nasceu em {nasc} tem {idade} anos em {atual}")
if idade == 18:
    print ("Voce tem que se alistar imediatamente")
elif idade < 18:
    saldo = 18 - idade 
    print (f"Voce ainda nao tem 18 anos. Ainda faltam {saldo} ano(s), para voce se alistar ")
    ano = atual + saldo
    print (f"Seu alistamento será em {ano} ")
elif idade > 18:
    saldo = idade - 18
    print (f"Você ja deveria ter se alistado há {saldo} anos")
    ano = atual - saldo
    print (f"Seu alistamento foi em {ano}")
     