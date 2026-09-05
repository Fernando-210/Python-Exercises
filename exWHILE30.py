num = cont = soma = 0
num = int(input("Digite um numero [999 para PARAR]: "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Digite um numero [999 para PARAR]: "))
print (f"Voce digitou {cont} numeros a soma dos numeros é {soma}")
print ("Acabou")
