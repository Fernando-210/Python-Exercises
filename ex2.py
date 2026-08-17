casa = float(input("Qual será o valor da casa?"))
salario = float(input("Qual o seu salario? R$"))
years = int(input("Em quantos anos será pago?"))
vpm = casa / (years*12)
minimo = salario * 30/100
print ((f"Para pagar um casa no valor de R${casa:.2f} em {years} anos"), end='')
print (f" a prestaçao será de {vpm:.2f}")
if vpm <= minimo:
    print ("Emprestimo CONCEDIDO")
else:
    print ("Emprestimo NEGADO")
    


